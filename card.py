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

  def __init__ (self, month: Month, type: Type, num: int) -> None:
    """
    Initialize a card.
    Args:
        month (Month): Month of the card.
        type: (Type): Type of the card.
    """
    self.month = month
    self.type = type
    self.num = num

  def init_cards():
    cards = []
    distribution = {
        Month.JAN: [Type.PLAIN, Type.PLAIN,  Type.RIBBON, Type.BRIGHT],
        Month.FEB: [Type.PLAIN, Type.PLAIN,  Type.RIBBON, Type.ANIMAL],
        Month.MAR: [Type.PLAIN, Type.PLAIN,  Type.RIBBON, Type.BRIGHT],
        Month.APR: [Type.PLAIN, Type.PLAIN,  Type.RIBBON, Type.ANIMAL],
        Month.MAY: [Type.PLAIN, Type.PLAIN,  Type.RIBBON, Type.ANIMAL],
        Month.JUN: [Type.PLAIN, Type.PLAIN,  Type.RIBBON, Type.ANIMAL],
        Month.JUL: [Type.PLAIN, Type.PLAIN,  Type.RIBBON, Type.ANIMAL],
        Month.AUG: [Type.PLAIN, Type.PLAIN,  Type.ANIMAL, Type.BRIGHT],
        Month.SEP: [Type.PLAIN, Type.PLAIN,  Type.RIBBON, Type.ANIMAL],
        Month.OCT: [Type.PLAIN, Type.PLAIN,  Type.RIBBON, Type.ANIMAL],
        Month.NOV: [Type.PLAIN, Type.RIBBON, Type.ANIMAL, Type.BRIGHT],
        Month.DEC: [Type.PLAIN, Type.PLAIN,  Type.PLAIN,  Type.BRIGHT]}
    for month, types in distribution.items():
      for i, t in enumerate(types):
        cards.append(Card(month, t, i))
    return cards

  def __repr__ (self) -> str:
    return f"Card({self.month}-{self.type}-{self.num})"

