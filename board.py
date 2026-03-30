from card import Card
import random

class Player:
  hand : list[Card]
  koikoi : bool

  def __init__ (self, hand : list[Card]) -> None:
    self.hand = hand
    self.koikoi = False

class Board:
  j1 : Player
  j2 : Player
  center : list[Card]
  deck : list[Card]

  def __init__ (self) -> None:
    d = Card.init_cards ()
    random.shuffle(d)
    self.j1 = Player(d[0:6])
    self.j2 = Player(d[6:12])
    self.center = d[12:18]
    self.deck   = d[18:]
