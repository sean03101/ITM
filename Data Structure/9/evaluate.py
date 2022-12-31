#
# Parse an expression, then evaluate it immediately
#

from expression import Expression
import parser

class EvalError(Exception):
  def __init__(self, msg):
    self.msg = msg

def evaluate(expr, vars):
  t = expr.type()
  if t == "number":
    return expr.data
  if t == "variable":
    if expr.data in vars:
      return vars[expr.data]
    else:
      raise EvalError("Undefined variable '%s'" % expr.data)
  if t == "unary":
    arg = evaluate(expr.left, vars)
    return -arg
  # it's a binary operation
  op = expr.data
  lhs = evaluate(expr.left, vars)
  rhs = evaluate(expr.right, vars)
  if op == "+":
    return lhs + rhs
  if op == "-":
    return lhs - rhs
  if op == "*":
    return lhs * rhs
  if op == "/":
    return lhs / rhs
  if op == "^":
    return lhs ** rhs
  assert false, "Unknown operation"
  
# --------------------------------------------------------------------

if __name__ == "__main__":
  variables = { "a": 19, "b" : -3 }
  print("SeoulTech superCalculator v1.9")
  while True:
    s = input("Enter an expression: ")
    if s is None or s.strip() == "":
      break
    try:
      expr = parser.parse(s)
      print("==> %s" % str(expr))
      print("==> %g" % evaluate(expr, variables))
    except parser.InputError as e:
      print("Error:", e.msg)
      print(s)
      print(" " * e.token.pos + "^")
    except EvalError as e:
      print("Error:", e.msg)

# --------------------------------------------------------------------
