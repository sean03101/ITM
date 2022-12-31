#
# Compute sine and cosine
# 16102275 Park Hyun Woo & 16102284 Lee Sung Ho
# Programming Project 2 Problem 3

import math

def sine(x):
    
    if x>=0.01 or x<=-0.01:
        return 2*sine(x/2)*cosine(x/2)
    
    else:
        return x-(math.pow(x,3))/6
    
def cosine(x):
    
    if x>=0.01 or x<=-0.01:
        return 1-2*(math.pow(sine(x/2),2))
    
    else:
        return 1-(math.pow(x,2))/2
    
    
def tabulate(a, b, step):
  print("%5s : %-10s %-10s %-10s %-10s" % ("x", "sine(x)", "cosine(x)",
                                      "math.sin(x)", "math.cos(x)"))
  for i in range(a, b+1):
    x = step * i
    print("%5g : %-10g %-10g %-10g %-10g" %
          (x, sine(x), cosine(x), math.sin(x), math.cos(x)))

if __name__ == "__main__":
      tabulate(-20, 20, 0.1)
