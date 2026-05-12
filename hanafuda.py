from human import Human
from engine import Engine

def play():
  p1 = Human(id_=0)
  p2 = Human(id_=1)
  engine = Engine(p1, p2)
  engine.run()

play()