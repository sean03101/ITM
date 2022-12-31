
from liststack import Stack
  
def matching(open, close):
  m = { '(' : ')', '{': '}', '[': ']' }
  return open in m and m[open] == close
  
def balancedSymbols(s):
  stack = Stack()

  for ch in s:
    if ch in "({[":
      stack.push(ch)
    elif ch in ")}]":
      if stack.is_empty() or not matching(stack.top(), ch):
        return False
      stack.pop()
    # ignore all other characters
  return stack.is_empty()

