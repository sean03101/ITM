#
# A circular doubly-linked list
#

class Node:
  def __init__(self, el, next=None, prev=None):
    self.el = el
    self.next = next
    self.prev = prev

  def __repr__(self):
    return "<" + repr(self.el) + ">"

class CircularList:
  def __init__(self, el):
     self.head = Node(el)
     self.tail = Node(None)
     self.tail.next=self.head
     self.head.prev=self.tail
     
  def first(self):
    if self.head == None:
        return {}
    return self.head
    
  def __repr__(self):
    if len(self)<=1:
        return {}
    res = "["
    p = self.head
    while p != self.tail:
      res = res +str(p.el)
      if p.next != self.tail:
        res += ", "
      p = p.next
    res += "]"
        
    return res

  def remove(self, p):
    p.prev.next = p.next
    p.next.prev = p.prev
    
  def __len__(self):
    count = 0
    p = self.head
    while p != self.tail:
      count = count + 1
      p = p.next
    
    return count 

  def insert(self, p, el):
   n = Node(el)
   n.prev = p.prev
   n.next = p.prev.next
   n.next.prev = n
   p.prev.next = n

    
  def append(self, x):
    self.insert(self.first(),x)
    
if __name__ == '__main__':
    A=CircularList(10)
    B=[1,2,3,4,1,4,2,4]
    for i in B:
        A.append(i)
    print(A)
