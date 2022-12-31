
class EmptyStackError(Exception):
  pass

class Stack():
  def __init__(self):
    self._data = []

  def is_empty(self):
    return len(self._data) == 0
  
  def top(self):
    if self.is_empty():
      raise EmptyStackError
    return self._data[-1]

  def pop(self):
    if self.is_empty():
      raise EmptyStackError
    return self._data.pop()

  def push(self, x):
    self._data.append(x)

