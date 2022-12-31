from itm421stack import print_stack

def first(n):
  second(n)
  second(n * n)

def second(m):
  three(m)
  three(m+1)
  three(m+2)

def three(z):
  print("In three(%d):" % z)
  print_stack()

first(13)
