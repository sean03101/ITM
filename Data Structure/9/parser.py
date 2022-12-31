#
# Parse string and generate expression tree
#

import tokens
from expression import Expression

class InputError(Exception):
  def __init__(self, msg, token):
    self.msg = msg
    self.token = token

def parse_item(tok):
  t = tok[0]
  tok.pop(0)
  if t.isNumber() or t.isIdentifier():
    return Expression(t.value)
  if not t.isSymbol("("):
    raise InputError("Expected number, variable, or '('", t)
  expr = parse_expression(tok)
  if not tok[0].isSymbol(")"):
    raise InputError("Expected operator or ')'", tok[0])
  tok.pop(0)
  return expr

def parse_factor(tok):
  t = tok[0]
  sign = -1 if t.isSymbol("-") else +1
  if t.isSymbol("+") or sign < 0:
    tok.pop(0)
  expr = parse_item(tok)
  while tok[0].isSymbol("^"):
    tok.pop(0)
    rhs = parse_factor(tok)
    expr = Expression("^", expr, rhs)
  return expr if sign > 0 else Expression("--", expr)
  
def parse_term(tok):
  expr = parse_factor(tok)
  t = tok[0]
  while t.isSymbol("*") or t.isSymbol("/"):
    tok.pop(0)
    rhs = parse_factor(tok)
    expr = Expression(t.value, expr, rhs)
    t = tok[0]
  return expr

def parse_expression(tok):
  expr = parse_term(tok)
  t = tok[0]
  while t.isSymbol("+") or t.isSymbol("-"):
    tok.pop(0)
    rhs = parse_term(tok)
    expr = Expression(t.value, expr, rhs)
    t = tok[0]
  return expr

def parse(s):
  toks = tokens.tokenize(s)
  expr = parse_expression(toks)
  if not toks[0].isStop():
    raise InputError("Expected operator or end of input", toks[0])
  return expr

# --------------------------------------------------------------------

if __name__ == "__main__":
  print("Expression parser")
  while True:
    s = input("Enter an expression: ")
    if s is None or s.strip() == "":
      break
    try:
      expr = parse(s)
      print("==> %s" % str(expr))
    except InputError as e:
      print("Error:", e.msg)
      print(s)
      print(" " * e.token.pos + "^")

# --------------------------------------------------------------------
