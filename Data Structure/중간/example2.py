from itm421stack import print_stack

def factorial(n):
  if n <= 1:
    print_stack()
    return 1
  else:
    return n * factorial(n - 1)  

factorial(4)
