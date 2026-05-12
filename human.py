from player import Player

class Human(Player):
  id_ : int

  def __init__(self, id_: int):
    super().__init__(id_)

  def play_phase_1(self, state : State, moves : list[Answer]):
    print("[PHASE 1]Enter the move to do")
    for i, move in enumerate(moves):
      if move.card_match == None:
        print(f'{i}: put {move.card_from} in the center')
      else:
        print(f'{i}: take {move.card_from} and {move.card_match}')
    id_move = int(input())
    return(moves[id_move])

  def play_phase_2(self, state : State, moves : list[Answer]):
    print("[PHASE 2]Enter the move to do")
    for i, move in enumerate(moves):
      if move.card_match == None:
        print(f'{i}: put {move.card_from} in the center')
      else:
        print(f'{i}: take {move.card_from} and {move.card_match}')
    id_move = int(input())
    return(moves[id_move])

  def play_phase_3(self, state : State, moves : list[int]):
    print("[PHASE 3]Enter the move to do")
    for move in moves:
      match (move):
        case 0: print("0: passiv continue")
        case 1: print("1: koikoi")
        case 2: print("2: stop")
    id_move = int(input())
    return(moves[id_move])
