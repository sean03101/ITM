#
# Parse an expression, then show it in prefix and postfix notation
#

from expression import Expression
import parser

def prefix(expr):
  t = expr.type()
  if t == "number":
    return "%g" % expr.data
  if t == "variable":
    return expr.data
  if t == "unary":
    return "(- " + prefix(expr.left) + ")"
  # it's a binary operation
  return ("(" + expr.data + " " + prefix(expr.left) +
          " " + prefix(expr.right) + ")")

def postfix(expr):
  t = expr.type()
  if t == "number":
    return "%g" % expr.data
  if t == "variable":
    return expr.data
  if t == "unary":
    return postfix(expr.left) + " chs"
  # it's a binary operation
  return (postfix(expr.left) + " " + postfix(expr.right) + " " + expr.data)

# --------------------------------------------------------------------

if __name__ == "__main__":
  print("Expression converter")
  while True:
    s = input("Enter an expression: ")
    if s is None or s.strip() == "":
      break
    try:
      expr = parser.parse(s)
      print("==> %s" % prefix(expr))
      print("==> %s" % postfix(expr))      
    except parser.InputError as e:
      print("Error:", e.msg)
      print(s)
      print(" " * e.token.pos + "^")

# --------------------------------------------------------------------
