from enum import Enum

class Month(Enum):
  JAN = 1
  FEB = 2
  MAR = 3
  APR = 4
  MAY = 5
  JUN = 6
  JUL = 7
  AUG = 8
  SEP = 9
  OCT = 10
  NOV = 11
  DEC = 12

class Type(Enum):
  PLAIN  = 0
  ANIMAL = 1
  RIBBON = 2
  BRIGHT = 3

class Card:
  month : Month
  type : Type

  def __init__ ( self, month: Month, type: Type) -> None:
    """
    Initialize a card.
    Args:
        month (Month): Month of the card.
        type: (Type): Type of the card.
    """
    self.month = month
    self.type = type

  def init_cards():
    cards = []
    distribution = {
      Month.JAN: [Type.BRIGHT, Type.RIBBON, Type.PLAIN, Type.PLAIN],
      Month.FEB: [Type.ANIMAL, Type.RIBBON, Type.PLAIN, Type.PLAIN],
      Month.MAR: [Type.BRIGHT, Type.RIBBON, Type.PLAIN, Type.PLAIN],
      Month.APR: [Type.ANIMAL, Type.RIBBON, Type.PLAIN, Type.PLAIN],
      Month.MAY: [Type.ANIMAL, Type.RIBBON, Type.PLAIN, Type.PLAIN],
      Month.JUN: [Type.ANIMAL, Type.RIBBON, Type.PLAIN, Type.PLAIN],
      Month.JUL: [Type.ANIMAL, Type.RIBBON, Type.PLAIN, Type.PLAIN],
      Month.AUG: [Type.BRIGHT, Type.ANIMAL, Type.PLAIN, Type.PLAIN],
      Month.SEP: [Type.ANIMAL, Type.RIBBON, Type.PLAIN, Type.PLAIN],
      Month.OCT: [Type.ANIMAL, Type.RIBBON, Type.PLAIN, Type.PLAIN],
      Month.NOV: [Type.BRIGHT, Type.ANIMAL, Type.RIBBON, Type.PLAIN],
      Month.DEC: [Type.BRIGHT, Type.PLAIN, Type.PLAIN, Type.PLAIN],
    }
    for month, types in distribution.items():
      for t in types:
        cards.append(Card(month, t))

    return cards

  def __repr__ (self) -> str:
    return f"Card({self.month}-{self.type})"
