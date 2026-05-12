from state import State

class View:
  hand: list[Card]
  side: list[Card]
  center: list[Card]
  opponent_side: list[Card]
  koikoi : bool

  def __init__(self, hand: list[Card], side: list[Card], center: list[Card], opponent_side: list[Card], koikoi : bool):
    self.hand = hand
    self.side = side
    self.center = center
    self.opponent_side = opponent_side
    self.koikoi = koikoi

class Answer:
  card_from: Card
  card_match: Card | None
  direction: int

  def __init__(self, card_from: Card, card_match: Card, direction: int):
    self.card_from = card_from
    self.card_match = card_match
    self.direction = direction

class Engine:
  state : State
  agents : dict[int, Player]

  def __init__(self, p1: Player, p2: Player):
    self.state = State(p1.id_, p2.id_)
    self.agents = {
      p1.id_: p1,
      p2.id_: p2
    }

  def move_card (self, card: Card, from_: list[Card], to_: list[Card]) -> None:
    from_.remove(card)
    to_.append(card)
    return

  def view_from_player (self, state : State) -> View:
    return View (
      state.current_player.hand,
      state.current_player.side,
      state.center,
      state.opponent_player.side,
      state.koikoi
    )

  def find_matches(self, card: Card, center: list[Card]) -> list[Card]:
    return [c for c in center if c.month == card.month]

  def generate_moves_phase_1 (self, hand: list[Card], center: list[Card]) -> list[Answer]:
    res = []
    for card in hand:
      matches = self.find_matches(card, center)
      if matches == []:
        res.append(Answer(card, None, 1))
      else:
        for match in matches:
          res.append(Answer(card, match, 0))
    return res

  def generate_moves_phase_2 (self, card: Card, center: list[Card]) -> list[Answer]:
    res = []
    matches = self.find_matches(card, center)
    if matches == []:
      res.append(Answer(card, None, 1))
    else:
      for match in matches:
        res.append(Answer(card, match, 0))
    return res

  def switch_player(self, state : State) -> State:
    tmp = state.current_player
    state.current_player = state.opponent_player
    state.opponent_player = tmp
    return state

  def phase_1(self, state: State, decision: Answer) -> State:
    if decision.direction == 1:
      self.move_card(decision.card_from, state.current_player.hand, state.center)
    else:
      self.move_card(decision.card_from, state.current_player.hand, state.current_player.side)
      self.move_card(decision.card_match, state.center, state.current_player.side)
    return state

  def phase_2(self, state : State, decision: Answer) -> State:
    if decision.direction == 1:
      self.move_card(decision.card_from, state.deck, state.center)
    else:
      self.move_card(decision.card_from, state.deck, state.current_player.side)
      self.move_card(decision.card_match, state.center, state.current_player.side)
    return state

  def phase_3(self, state: State, decision: int, new_points: int) -> State:
    match decision:
      case 0: # passiv continue
        return state
      case 1: # koikoi
        state.koikoi = True
        return state
      case 2: # stop
        state.end = True
        state.current_player.points = new_points
        return state
      case _: return state

  def generate_moves_decision(self, state : State, new_points: int) -> list[int]:
    res = []
    if state.current_player.points < new_points:
      res = [1, 2] # 1 -> koikoi # 2 -> stop
    else:
      res = [0] # 0 -> passiv continue
    return res


  def play_turn(self, state : State) -> State:
    current_agent = self.agents[state.current_player.id_]
    # phase 1
    ans = current_agent.play_phase_1(self.view_from_player(state), self.generate_moves_phase_1(state.current_player.hand, state.center))
    s1 = self.phase_1(state, ans)
    # phase 2
    ans = current_agent.play_phase_2(self.view_from_player(state), self.generate_moves_phase_2(state.deck[0], state.center))
    s2 = self.phase_2(s1, ans)
    # phase 3
    new_points = state.eval_side(state.current_player.side, state.koikoi)
    ans = current_agent.play_phase_3(self.view_from_player(state), self.generate_moves_decision(state, new_points))
    s3 = self.phase_3(s2, ans, new_points)
    return s3

  def play_turns(self, state : State) -> State:
    while (not state.end) and (state.opponent_player.hand != []):
      if state.end:
        print(f'win with {state.current_player.points}')
        break
      if state.opponent_player.hand == []:
        print("no ones won")
        break
      state = self.switch_player(state)
      state = self.play_turn(state)
    return state

  def run(self):
    print("Starting the game...")
    self.play_turns(self.state)