from board import Board
import random

def game ():
  random.seed(1)
  board = Board ()
  print(len(board.center))
  print(len(board.j1.hand))
  print(len(board.j2.hand))
  print(len(board.deck))

game ()
