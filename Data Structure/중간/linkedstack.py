
class EmptyStackError(Exception):
  pass

class _Node():
  def __init__(self, el, next):
    self.el = el
    self.next = next

class Stack():
  def __init__(self):
    self._tos = None

  def is_empty(self):
    return self._tos is None
  
  def top(self):
    if self.is_empty():
      raise EmptyStackError
    return self._tos.el

  def pop(self):
    if self.is_empty():
      raise EmptyStackError
    el = self._tos.el
    self._tos = self._tos.next
    return el

  def push(self, x):
    self._tos = _Node(x, self._tos)


