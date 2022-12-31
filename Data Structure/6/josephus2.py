import sys
#from circularlist import CircularList
from solution import CircularList

def josephus(n, m):
  L = CircularList('A')
  for i in range(2, n+1):
    L.append(chr(ord('A') + i - 1))
  p = L.first()
  for i in range(n-1):
    print(L, p.el)
    for j in range(m):
      p = p.next
    q = p
    p = p.next
    L.remove(q)
  return L.first().el

result = josephus(int(sys.argv[1]), int(sys.argv[2]))
print("The last one is ", result)
