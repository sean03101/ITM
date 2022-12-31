#
# Implementation of dict using a Binary Search Tree
#  WITHOUT recursion for insertion and deletion
#

class _Node():
  def __init__(self, key, value, left=None, right=None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right

  # This method is still recursive
  # We will only use it for small trees to test your methods
  def _description(self, level):
    ls = self.left._description(level+1) if self.left else ""
    rs = self.right._description(level+1) if self.right else ""
    return ls + str(self.key) + ("(%d) " % level) + rs

  def _find_first(self):
    p = self
    while p.left is not None:
      p = p.left
    return p

  def _find_last(self):
    p = self
    while p.right is not None:
      p = p.right
    return p

  def _find(self, key):
    p = self
      
    while p.key != key:
        if p.key < key :
            p = p.left
            if p is None:
                return None
                break
                    
        else:
            p = p.right
            if p is None:
                return None
                break
            
    return p

  def _insert(self, key, value):
   
    while self is not None: 
        
        if key == self.key:
            
          self.value = value
          break
      
        elif key < self.key:
            
          if self.left is None:
            self.left = _Node(key, value)
            break
          else:
            self = self.left
          
        else:
          if self.right is None:
              self.right =_Node(key,value)
              break
          else:
              self = self.right
    
  # Remove node with smallest key in the subtree rooted at this node
  # Returns the new root.
  def _remove_first(self):
    p = self
    
    if p.left is None:
        return self.right
    else:
        while p.left.left is not None:
            p = p.left
        
        if p.left.right is not None:
            p.left = p.left.right
        else:
            p.left = None
            
        return self
        
    

  # Returns the new root.
  def _remove(self, key):
    p = self
    
    if self.key == key:
        if self.right is not None and self.left is not None:
            
            n = self.right._find_first()
            
            self.key = n.key
            self.value = n.value
            
            self.right = self.right._remove_first()
            
            return self
        
        else:
            if self.right is None and self.left is None:
                return None
            else:
                return self.left if self.left else self.right
            
            
        
    while p.key != key:
        if key<p.key and p.left is not None:
            if p.left.key == key:
                if p.left.right is None and p.left.left is None:          
                    p.left = None
                    return self
                    break
                elif p.left.right is None and p.left.left is not None:
                    p.left = p.left.left
                    return self
                    break
                elif p.left.right is not None and p.left.left is None:
                    p.left = p.left.right
                    return self
                    break
                else:
                    n = p.left.right._find_first()
                  
                    p.left.key = n.key
                    p.left.value = n.value
                    
                    p.left.right = p.left.right._remove_first()
                    
                    return self
                    break
            else:
                p = p.left
                
        elif key>p.key and p.right is not None:
            if p.right.key == key :
                if p.right.right is None and p.right.left is None:
                    p.right = None
                    return self
                    break
                elif p.right.right is None and p.right.left is not None:
                    p.right = p.right.left
                    return self
                    break
                elif p.right.right is not None and p.right.left is None:
                    p.right = p.right.right
                    return self
                    break
                else:
                    n = p.right.right._find_first()

                    p.right.key = n.key
                    p.right.value = n.value
                    
                    p.right.right = p.right.right._remove_first()
                    
                    return self
                    break
            else:
                p = p.right
                
        else:
            return self
            break
        
    
    

# --------------------------------------------------------------------

class dict():
  def __init__(self):
    self._root = None

  def __str__(self):
    return self._root._description(0) if self._root else "[]"

  def _find(self, key):
    return self._root._find(key) if self._root else None

  def __getitem__(self, key):
    n = self._find(key)
    if n is None:
      raise KeyError(key)
    return n.value 

  def get(self, key, v = None):
    n = self._find(key)
    return n.value if n else v

  def __contains__(self, key):
    return self._find(key) is not None

  def __setitem__(self, key, value):
    if self._root is None:
      self._root = _Node(key, value)
    else:
      self._root._insert(key, value)

  def firstkey(self):
    return self._root._find_first().key if self._root else None

  def lastkey(self):
    return self._root._find_last().key if self._root else None

  def __delitem__(self, key):
    if self._root:
      self._root = self._root._remove(key)

# --------------------------------------------------------------------