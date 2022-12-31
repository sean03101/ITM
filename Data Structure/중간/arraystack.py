
class EmptyStackError(Exception):
  pass

class StackOverflow(Exception):
  pass

class Stack():
  def __init__(self, capacity):
    self._data = [ None ] * capacity
    self._tos = -1

  def is_empty(self):
    return self._tos == -1
  
  def top(self):
    if self.is_empty():
      raise EmptyStackError
    return self._data[self._tos]

  def pop(self):
    if self.is_empty():
      raise EmptyStackError
    el = self._data[self._tos]
    self._tos -= 1
    return el

  def push(self, x):
    if self._tos + 1 == len(self._data):
      raise StackOverflow
    self._tos += 1
    self._data[self._tos] = x
