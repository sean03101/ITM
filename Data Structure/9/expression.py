#
# Expression trees
#

class Expression():
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def type(self):
    if type(self.data) in [int, float]:
      return "number"
    if self.data in [ "+", "-", "*", "/", "^" ]:
      return "binop"
    if self.data == "--":
      return "unary"
    return "variable"

  def __str__(self):
    t = self.type()
    if t == "number":
      return str(self.data)
    if t == "variable":
      return self.data
    if t == "unary":  # unary minus
      return "-" + str(self.left)
    # it's a binary operation
    return "(" + str(self.left) + " " + self.data + " " + str(self.right) + ")"

# --------------------------------------------------------------------

if __name__ == '__main__':
  e = Expression("*", 
                 Expression("a"),
                 Expression("--", 
                            Expression("+",
                                       Expression(2),
                                       Expression("-",
                                                  Expression("b"),
                                                  Expression(7)))))
  print(e)

# --------------------------------------------------------------------
