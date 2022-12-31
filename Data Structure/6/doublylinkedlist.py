class EmptyListError(Exception):
  pass

class Node:
  def __init__(self, el, next=None, prev=None):
    self.el = el
    self.next = next
    self.prev = prev

  def __repr__(self):
    return "<" + repr(self.el) + ">"

class DoublyLinkedList:
  def __init__(self):
    self._front = Node(None)
    self._rear = Node(None, prev=self._front)
    self._front.next = self._rear
  
  def is_empty(self):
    return self._front.next == self._rear

  def first(self):
    if self.is_empty():
      raise EmptyListError
    return self._front.next

  def last(self):
    if self.is_empty():
      raise EmptyListError
    return self._rear.prev

  def __repr__(self):
    res = "["
    p = self._front.next
    while p != self._rear:
      res += str(p.el)
      if p.next != self._rear:
        res += ", "
      p = p.next
    res += "]"
    return res

  def __len__(self):
    p = self._front.next
    count = 0
    while p != self._rear:
      count += 1
      p = p.next
    return count

  def insert_after(self, n, el):
    p = Node(el, n.next, n)
    n.next.prev = p
    n.next = p

  def prepend(self, el):
    self.insert_after(self._front, el)
  
  def append(self, el):
    self.insert_after(self._rear.prev, el)

  def remove(self, n):
    n.prev.next = n.next
    n.next.prev = n.prev

  def find_first(self, x):
    
    if len(self)==0:
        return {}
      
    first = self.first()
    
    if first.el == x:
        return first
    
    else:
        B=first
        result = None
        for i in range(0,len(self)-1):
            B=B.next
            if(B.el==x):
                result = B
                break
  
    return result
            
    
      
  def find_last(self, x):
    
    if self.is_empty():
      return {}
        
        
    last =self.last()
    
    if last.el == x:
        return last
    
    else:
        B=last
        result = None
        for i in range(0,len(self)-1):
            B=B.prev
            if(B.el==x):
                result = B
                break
  
    return result

  def count(self, x):
    if self.is_empty():
      raise EmptyListError
        
    first=self.first()
    
    result=0
    B=first
    for i in range(0,len(self)-1):
         B=B.next
         if(B.el==x):
             result=result+1
             
    return result

  def remove_first(self, x):
    if self.is_empty():
      return {}
        
    else:
        A=self.find_first(x)
        if A==None:
            self
        else:   
            A.prev.next = A.next
            A.next.prev = A.prev


  def remove_last(self, x):
    if self.is_empty():
      return {}
        
    A=self.find_last(x)
    if A==None:
        self
    else:
        A.prev.next = A.next
        A.next.prev = A.prev


  def remove_all(self, x):
    if self.is_empty():
      return {}
        
    for i in range(0,self.count(x)+1):
        self.remove_first(x)

      
  def takeout(self, n, m):
      new = DoublyLinkedList()
