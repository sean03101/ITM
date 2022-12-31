#
# Unit tests for DoublyLinkedList
#

import unittest
import time, sys
if sys.argv[-1] == "solution":
  import solution as sol
else:
  import doublylinkedlist as sol

# --------------------------------------------------------------------

consmsg = "Your code has broken the structure of the doubly-linked list."

def make(*els):
  a = sol.DoublyLinkedList()
  for e in els:
    a.append(e)
  return a

def makeFrom(els):
  a = sol.DoublyLinkedList()
  for e in els:
    a.append(e)
  return a

def nodeIndex(a, n):
  i = 0
  p = a._front.next
  while p != a._rear:
    if p is n:
      return i
    p = p.next
    i += 1
  return -1

def goto(a, idx):
  p = a._front.next
  while idx > 0:
    p = p.next
    idx -= 1
  return p

# --------------------------------------------------------------------

class TestDoublyLinkedList(unittest.TestCase):

  def checkNode(self, a, meth, x, idx, pts):
    if meth == "first":
      r = a.find_first(x)
    else:
      r = a.find_last(x)
    if idx == -1:
      self.assertIsNone(r)
    else:
      self.assertEqual(nodeIndex(a, r), idx)

  def checkCount(self, a, x, res, pts):
    r = a.count(x)
    self.assertEqual(r, res)

  def consistency(self, a):
    if a.is_empty():
      self.assertIs(a._front.next, a._rear, msg=consmsg)
      self.assertIs(a._rear.prev, a._front, msg=consmsg)
    else:
      p = a._front
      while p != a._rear:
        self.assertIs(p.next.prev, p, msg=consmsg)
        p = p.next

  def check(self, a, op, pts, ref):
    op(a)
    self.consistency(a)
    self.assertEqual(str(a), ref)

  def checkTakeOut(self, a, i, j, pts, resa, resb):
    n = goto(a, i)
    m = goto(a, j)
    b = a.takeout(n, m)
    self.consistency(a)
    self.consistency(b)
    self.assertIs(n, b._front.next)
    self.assertIs(m, b._rear.prev)
    self.assertEqual(str(a), resa)
    self.assertEqual(str(b), resb)    
    
  def test_findfirst(self):
    a = make(99, 27, 13, 13, 27, 99, 99, 99, 27, 1, 29, 13, 17, 27, 88)
    self.checkNode(a, "first", 99, 0, 2)
    self.checkNode(a, "first", 13, 2, 2)
    self.checkNode(a, "first", 1, 9, 2)
    self.checkNode(a, "first", 88, 14, 2)
    self.checkNode(a, "first", 42, -1, 1)

  def test_findlast(self):
    a = make(99, 27, 13, 13, 27, 99, 99, 99, 27, 1, 29, 13, 17, 27, 88)
    self.checkNode(a, "last", 88, 14, 2)
    self.checkNode(a, "last", 99, 7, 2)
    self.checkNode(a, "last", 1, 9, 2)
    self.checkNode(a, "last", 42, -1, 1)

  def test_count(self):
    a = make(99, 27, 13, 13, 27, 99, 99, 99, 27, 1, 29, 13, 17, 27, 88)
    self.checkCount(a, 13, 3, 4)
    self.checkCount(a, 37, 0, 4)
    self.checkCount(a, 88, 1, 4)

  def test_remove(self):
    a = make(99, 27, 13, 13, 27, 99, 99, 99, 27, 1, 29, 13, 17, 27, 88)
    self.check(a, lambda x : x.remove_first(99), 4,
               "[27, 13, 13, 27, 99, 99, 99, 27, 1, 29, 13, 17, 27, 88]")
    self.check(a, lambda x : x.remove_first(88), 4,
               "[27, 13, 13, 27, 99, 99, 99, 27, 1, 29, 13, 17, 27]")
    self.check(a, lambda x : x.remove_last(99), 4,
               "[27, 13, 13, 27, 99, 99, 27, 1, 29, 13, 17, 27]")
    self.check(a, lambda x : x.remove_last(37), 4,
               "[27, 13, 13, 27, 99, 99, 27, 1, 29, 13, 17, 27]")
    self.check(a, lambda x : x.remove_first(42), 4,
               "[27, 13, 13, 27, 99, 99, 27, 1, 29, 13, 17, 27]")
    self.check(a, lambda x : x.remove_first(1), 4,
               "[27, 13, 13, 27, 99, 99, 27, 29, 13, 17, 27]")
    self.check(a, lambda x : x.remove_all(13), 4,
               "[27, 27, 99, 99, 27, 29, 17, 27]")
    self.check(a, lambda x : x.remove_all(27), 4,
               "[99, 99, 29, 17]")
    
  def test_remove_empty(self):
    b = make()
    self.check(b, lambda x : x.remove_all(27), 2, "[]")
    self.check(b, lambda x : x.remove_first(13), 2, "[]")
    self.check(b, lambda x : x.remove_last(99), 2, "[]")
    
  def test_takeout(self):
    a = make(99, 27, 13, 13, 27, 99, 99, 99, 27, 1, 29, 13, 17, 27, 88)
    self.checkTakeOut(a, 4, 9, 5,
                      "[99, 27, 13, 13, 29, 13, 17, 27, 88]",
                      "[27, 99, 99, 99, 27, 1]")
    self.checkTakeOut(a, 0, 8, 5,
                      "[]", "[99, 27, 13, 13, 29, 13, 17, 27, 88]")
    a = make(99, 12, 13, 44, 55)
    self.checkTakeOut(a, 2, 2, 4,
                      "[99, 12, 44, 55]", "[13]")
    self.checkTakeOut(a, 1, 3, 5,
                      "[99]", "[12, 44, 55]")
    a = makeFrom(range(1000))
    self.checkTakeOut(a, 0, 10, 5,
                      str(list(range(11, 1000))),
                      str(list(range(11))))
    self.checkTakeOut(a, 100, 500, 10,
                      str(list(range(11, 111)) + 
                          list(range(512, 1000))),
                      str(list(range(111, 512))))

  def test_constant_time(self):
    # try to check if takeout really works in constant time
    a = makeFrom(range(1000000))
    n = goto(a, 200000)
    m = goto(a, 600000)
    t0 = time.perf_counter()
    b = a.takeout(n, m)
    t1 = time.perf_counter()
    self.assertLess(t1 - t0, 0.001, msg="Your takeout function doesn't seem to work in constant time")
    
# --------------------------------------------------------------------
    
if __name__ == '__main__':
  unittest.main(verbosity=2, argv=sys.argv[:1])

# --------------------------------------------------------------------


