#
# 
# DoublyLinkedList with Mergesort
# 16102275 Park Hyun Woo & 16102284 Lee Sung Ho
# Programming Project 8

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
  def __init__(self, *els):
    self._front = Node(None)
    self._rear = Node(None, prev=self._front)
    self._front.next = self._rear
    for el in els:
      self.append(el)
  
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

# --------------------------------------------------------------------

  def median(self):
    if self.is_empty():
        return []
    else:
        left = self.first()
        right = self.last()
        
        while left != right:
            if left.next == right:
                return left
                break
            
            left = left.next
            right = right.prev
            
        return left
    
  def split(self, n):
    "Removes all nodes after n from this list and returns them in a new DoublyLinkedList object."
    new = DoublyLinkedList()
    
    new._front.next = n.next
    n.next.prev =new._front
    
    new._rear.prev = self._rear.prev
    self._rear.prev.next = new._rear
    
    self._rear.prev = n
    n.next = self._rear
    
    
    
    return new
         
  def steal(self, other):
    "Moves first node in other list to the end of this list."
    
    other._front.next.prev = self._rear.prev    
    
    self._rear.prev.next = other._front.next
    self._rear.prev = other._front.next
    
    other._front.next.next.prev = other._front
    
    A = other._front.next.next

    other._front.next.next = self._rear
    other._front.next = A
        
    
        
   
         
  def merge(self, other):
    "Merges elements from sorted other list into this sorted list."
    left = self.split(self._front)  # move all elements to a new list
    # now merge left and other
    if not left.is_empty() and not other.is_empty():
        while not left.is_empty() and not other.is_empty():
                A = left.first()
                B = other.first()
                
                if A.el>B.el:
                    self.steal(other)
                else:
                    self.steal(left)
            
        if left.is_empty():
            while True:
                self.steal(other)
                if other.is_empty():
                    break
                
        elif other.is_empty():
            while True:
                self.steal(left)
                if left.is_empty():
                    break
        
    
    elif left.is_empty() and not other.is_empty():
        for i in range(len(other)):
            self.steal(other)
        
    elif not left.is_empty() and other.is_empty():
        
        for i in range(len(left)):
            self.steal(left)
        
    else:
        self
            
# ——————————————————————————————————

  def sort(self):
    # is length <= 1 ?
    if self.is_empty() or self._front.next.next == self._rear:
      return
    other = self.split(self.median())
    self.sort()
    other.sort()
    self.merge(other)

