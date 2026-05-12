import abc

class Player(metaclass=abc.ABCMeta):
  id_: int

  def __init__(self, id_: int):
    self.id_ = id_

  @abc.abstractmethod
  def play_phase_1(self, state : State, moves : list[Answer]):
    """Play the phase 1"""
    raise NotImplementedError

  @abc.abstractmethod
  def play_phase_2(self, state : State, moves : list[Answer]):
    """Play the phase 1"""
    raise NotImplementedError

  @abc.abstractmethod
  def play_phase_3(self, state : State, moves : list[int]):
    """Play the phase 1"""
    raise NotImplementedError
