from card import Card, Type, Month
import random

class PlayerData:
  id_ : int
  hand : list[Card]
  side : list[Card]
  points : int

  def __init__(self, id: int, hand: list[Card]):
    self.id_ = id
    self.hand = hand
    self.side = []
    self.points = 0

class State:
  current_player : PlayerData
  opponent_player : PlayerData
  deck : list[Card]
  center : list[Card]
  koikoi : bool
  end : bool

  def __init__(self, p1_id, p2_id):
    d = Card.init_cards()
    random.shuffle(d)
    self.current_player = PlayerData(p1_id, d[0:6])
    self.opponent_player = PlayerData(p2_id, d[6:12])
    self.center = d[12:18]
    self.deck   = d[18:]
    self.koikoi = False
    self.end = False
    # todo : check if the game is playable

  def eval_side (self, side : list[Card], koikoi: bool) -> int:
    count = 0
    points = [
      0,  # plain
      0,  # animals
      0,  # inoshikacho
      0,  # ribbons
      0,  # poet ribbons
      0,  # blue ribbons
      0,  # sake moon
      0,  # sake curtain
      0,  # bright
      0   # rainman
    ]
    for card in side:
      match card.type:
        case Type.PLAIN:
          points[0] = points[0] + 1
        case Type.ANIMAL:
          points[1] = points[1] + 1
          if card.month == Month.JUL or card.month == Month.OCT or card.month == Month.JUN:
            points[2] = points[2] + 1
          if card.month == Month.SEP:
            points[6] = points[6] + 1
            points[7] = points[7] + 1
        case Type.RIBBON:
          points[3] = points[3] + 1
          if card.month == Month.JAN or card.month == Month.FEB or card.month == Month.MAR:
            points[4] = points[4] + 1
          if card.month == Month.JUN or card.month == Month.SEP or card.month == Month.OCT:
            points[5] = points[5] + 1
        case Type.BRIGHT:
          if card.month == Month.AUG:
            points[6] = points[6] + 1
          if card.month == Month.MAR:
            points[7] = points[7] + 1
          if card.month == Month.NOV:
            points[9] = points[9] + 1
          points[8] = points[8] + 1
    plain = points[0] - 9 if points[0] >= 10 else 0
    animals = points[1] - 4 if points[1] >= 5 else 0
    inoshikacho =  5 + points[1] if points[2] == 3 else 0
    ribbons = points[3] - 4 if points[3] >= 5 else 0
    poet = 5 + points[3] if points[4] == 3 else 0
    blue = 5 + points[3] if points[5] == 3 else 0
    bluepoet = 10 + points[3] if points[4] == 3 and points[5] == 3 else 0
    sakemoon = 5 if points[6] == 2 else 0
    sakecurtain = 5 if points[7] == 2 else 0
    bright = 15 if points[8] == 5 else 6 if points[8] == 3 else 7 if points[8] == 4 and points[9] == 1 else 8 if points[8] == 4 else 0
    score = plain + animals + inoshikacho + ribbons + poet + blue + bluepoet + sakemoon + sakecurtain + bright
    print(f'-----\nplain:{points[0]}\nanimals:{points[1]}\ninoshikacho:{points[2]}\nribbons:{points[3]}\npoet:{points[4]}\nblue:{points[5]}\nsakemoon:{points[6]}\nsakefleur:{points[7]}\nbright:{points[8]}\nrainman:{points[9]}\n-----> score = {score}')
    if score >= 7:
      score = score * 2
    if koikoi:
      score = score * 2
    return score