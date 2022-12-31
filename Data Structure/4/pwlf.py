#
# A class representing a piecewise linear function
## 16102275 Park Hyun Woo & 16102284 Lee Sung Ho
# --------------------------------------------------------------------
import copy

class PieceWiseLinear(object):
  """A piecewise linear function"""
  def __init__(self, x0, y0, x1, y1):
    if x1 <= x0:
      raise ValueError("x1 must be larger than x0")
    else:
      self.a=[[x0,y0],[x1,y1]]
      self.x0=x0
      self.y0=y0
      self.x1=x1
      self.y1=y1
      
      
  def domain(self):
    """Return domain interval as a pair."""
   
    a= self.x0,self.x1
    
    return a
                    
  def __str__(self): #객체를 문자열화 할때 쓴다
      b1 ="(%g,%g)..(%g,%g)"%(self.a[0][0],self.a[0][1],self.a[1][0],self.a[1][1])
      if len(self.a)>2:
          for i in range(2,len(self.a)):
              b1=b1+"..(%g,%g)"%(self.a[i][0],self.a[i][1])
      
      return b1
      
  def __call__(self, x):
    """Evaluate this function at x-coordinate x."""
    d = self.domain()
    if x < d[0] or x > d[1]:
      raise ValueError("argument is not in domain")
    else:
        for i in range(0,len(self.a)):
             if(x<=self.a[i][0]):
                  if(i!=0):   
                     return self.a[i-1][1]+(x-self.a[i-1][0])*(self.a[i][1]-self.a[i-1][1])/(self.a[i][0]-self.a[i-1][0])
                     break;
                  else:
                     return self.a[0][1] 
  
  def join(self, rhs):
    """Join two piecewise linear functions."""
    d1= self.domain()
    d2 = rhs.domain()
    if d1[1] != d2[0]:
      raise ValueError("domains are not contiguous")
    if abs(self(d1[1]) - rhs(d2[0])) > 1e-13:
      raise ValueError("discontinuity at connection point")
    
    new = PieceWiseLinear(0,0,1,1)
    new.a=copy.deepcopy(self.a)
    for i in range(1,len(rhs.a)):
        b=[rhs.a[i][0],rhs.a[i][1]]
        new.a.append(b)
        
    new.y0=copy.deepcopy(self.y0)
    new.y1=copy.deepcopy(rhs.y1)
    new.x1=copy.deepcopy(rhs.x1)
    new.x0=copy.deepcopy(self.x0)
    return new

    

        
        
        
  def __rmul__(self, lhs):
    new1 =PieceWiseLinear(0,0,1,1)
    new1.a= copy.deepcopy(self.a)
    
    for i in range(0,len(self.a)):
        new1.a[i][1]= self.a[i][1]*lhs

    new1.x0=self.x0
    new1.x1=self.x1
    new1.y0=self.y0*lhs
    new1.y1=self.y1*lhs
    
    return new1

  def add_pwlf(self, rhs, factor):
    """Returns the sum of this function and factor * rhs,
where rhs is another piecewise linear function.
The domain of the result is the intersection of the two domains.
Returns a new function, this function remains unchanged."""
    x0a, x1a = self.domain()
    x0b, x1b = rhs.domain()
    x0 = max(x0a, x0b)
    x1 = min(x1a, x1b)
    
    if x0 >= x1:
      raise ValueError("domains do not overlap")
      
    new=PieceWiseLinear(0,0,1,1)
    new.x0=x0
    new.x1=x1
    new.y0=self(x0)+factor*rhs(x0)
    new.y1=self(x1)+factor*rhs(x1)
    
    A=copy.deepcopy(self.a)
    B=copy.deepcopy(rhs.a)
    
    C=[]
    
    for i in range(0,len(A)):
         C.append(A[i][0])
    
    for i in range(0,len(B)):
         C.append(B[i][0])
    
    C=list(set(C))#중복제거
    C=sorted(C)
    
  
    for i in range(0,len(C)):
        if C[i]==x0:
            first=i
        elif C[i]==x1:
            last=i
            
    #new.a=[[0 for i in range(first,last+1)]  for j in range (first,last+1)]#배열초기화
    k=0
    new.a=[]
    for i in range(first,last+1):
        new.a.append([C[i],self(C[i])+factor*rhs(C[i])])
        k=k+1
    
    return new

  def add_number(self, rhs, factor):
    """Returns the sum of this function and factor * rhs,
where rhs is a number.
This function remains unchanged."""
    
    new4 =PieceWiseLinear(0,0,1,1)
    new4.a=copy.deepcopy(self.a)
    for i in range(0,len(self.a)):
       new4.a[i][1]= new4.a[i][1]+factor*rhs
    
    new4.x0=self.x0
    new4.x1=self.x1
    new4.y1=self.y1+rhs*factor
    new4.y0=self.y0+rhs*factor
    
    return new4
    

  def __add__(self, rhs):
    """Addition of a piecewise linear function with a number or 
with another piecewise linear function.
Returns a new function, this function remains unchanged."""
    if isinstance(rhs, PieceWiseLinear):
      return self.add_pwlf(rhs, +1)
    else:
      return self.add_number(rhs, +1)

  def __sub__(self, rhs):
    """Subtraction of a number or of another piecewise linear function
from this piecewise linear function.
Returns a new function, this function remains unchanged."""
    if isinstance(rhs, PieceWiseLinear):
      return self.add_pwlf(rhs, -1)
    else:
      return self.add_number(rhs, -1)
  
# --------------------------------------------------------------------

if __name__ == "__main__":
  f1 = PieceWiseLinear(1, -1, 3, 1)
  f2 = PieceWiseLinear(3, 1, 7, -5)
  print("f1 = %s" % f1)
  print("f2 = %s" % f2)  
  for x in [1, 2, 3]:
    print("f1(%g) = %g" % (x, f1(x)))
  for x in [3, 5, 7]:
    print("f2(%g) = %g" % (x, f2(x)))
  f = f1.join(f2)
  print("f = %s" % f) 
  for x in [1, 2, 3, 5, 7]:
    print("f(%g) = %g" % (x, f(x)))
  print("Domain of f1 = %s, domain of f2 = %s, domain of f = %s" %
        (f1.domain(), f2.domain(), f.domain()))
  g1 = f + 2
  print("g1 = f + 2 = %s" % g1)
  print(f)
  g2 = f - 6
  print("g2 = f - 6 = %s" % g2)
  g3 = 3 * f
  print("g3 = 3 * f = %s" % g3)
  h1 = 5 * f + 3
  h2 = 0.5 * f - 2
  print("h1 = 5 * f + 3 = %s" % h1)
  print("h2 = 0.5 * f - 2 = %s" % h2)
  
  g = h1 + h2
  print("g = h1 + h2 = %s" % g)
  d1 = PieceWiseLinear(0, 0, 2, 19)
  d = d1.join(PieceWiseLinear(2, 19, 6, 12))
  print("d = %s" % d)
  e1 = g + d
  e2 = g - d
  print("e1 = g + d = %s" % e1)
  print("e2 = g - d = %s" % e2)  
  for x in [1, 2, 3, 4, 5, 6]:
    print("g(%g) = %g, d(%g) = %g, e1(%g) = %g, e2(%g) = %g" %
          (x, g(x), x, d(x), x, e1(x), x, e2(x)))

# --------------------------------------------------------------------
