#
# Unit tests for merge sort for linked lists
#

import unittest
import random, time, sys
if sys.argv[-1] == "solution":
  import solution as sol
else:
  import listsort as sol

# --------------------------------------------------------------------

consmsg = "The structure of the linked list is broken."

class TestListSort(unittest.TestCase):

  def make_simple(self):
    s = sol.DoublyLinkedList("ITM421", "is", "a", "lot", "of", "fun",
                             "a", "lot", "of", "fun", "is", "ITM421")
    return s

  def index(self, s, q):
    i = 0
    p = s.first()
    while p is not s._rear:
      if p is q:
        return i
      i += 1
      p = p.next
    return -1

  def consistency(self, s):
    self.assertFalse(s.is_empty())
    p = s._front
    self.assertEqual(p, s.first().prev, consmsg)
    self.assertEqual(p.prev, None, consmsg)
    self.assertEqual(p.next, s.first(), consmsg)
    rear = s._rear
    self.assertEqual(rear, s.last().next, consmsg)
    self.assertEqual(rear.next, None, consmsg)
    self.assertEqual(rear.prev, s.last(), consmsg)
    while p is not rear:
      self.assertEqual(p.next.prev, p, consmsg)
      p = p.next

  def compare(self, s, t):
    self.consistency(s)
    p = s.first()
    i = 0
    rear = s._rear
    while i < len(t):
      self.assertNotEqual(p, rear)
      self.assertEqual(p.el, t[i])
      i += 1
      p = p.next
    self.assertEqual(p, rear)
  
  def test_median(self):
    s = self.make_simple()
    self.assertEqual(s.median().el, "fun")
    self.assertEqual(self.index(s, s.median()), 5)
    s.append("ITM411")
    self.assertEqual(self.index(s, s.median()), 6)

  def test_split(self):
    s = self.make_simple()
    b = s.split(s.first().next.next)
    self.compare(s, ["ITM421","is","a"])
    self.compare(b, ["lot","of","fun","a","lot","of","fun","is","ITM421"])
    c = b.split(b.last())
    self.assertTrue(c.is_empty())
    self.compare(b, ["lot","of","fun","a","lot","of","fun","is","ITM421"])
    d = b.split(b.median())
    self.compare(b, ["lot","of","fun","a","lot"])
    self.compare(d, ["of","fun","is","ITM421"])
    e = d.split(d.first().prev)  # split on front sentinel
    self.assertTrue(d.is_empty())
    self.compare(e, ["of","fun","is","ITM421"])

  def test_steal(self):
    s = sol.DoublyLinkedList()
    t = sol.DoublyLinkedList()
    t.append(13)
    t.append(27)
    n1 = t.first()
    s.steal(t)
    self.assertEqual(s.last(), n1)
    self.compare(s, [13])
    self.compare(t, [27])
    n2 = t.first()
    s.steal(t)
    self.assertEqual(s.last(), n2)
    self.compare(s, [13, 27])
    self.assertTrue(t.is_empty())

  def checkMerge(self, a, b, ab):
    a.merge(b)
    self.assertTrue(b.is_empty())
    if len(ab) == 0:
      self.assertTrue(a.is_empty())
    else:
      self.compare(a, ab)
                 
  def test_merge(self):
    self.checkMerge(sol.DoublyLinkedList(),
                    sol.DoublyLinkedList(),
                    [])
    self.checkMerge(sol.DoublyLinkedList(),
                    sol.DoublyLinkedList(1, 13),
                    [1, 13])
    self.checkMerge(sol.DoublyLinkedList(2, 17),
                    sol.DoublyLinkedList(),
                    [2, 17])
    self.checkMerge(sol.DoublyLinkedList(1, 3, 13, 17, 25),
                    sol.DoublyLinkedList(2, 5, 6, 8, 15, 29),
                    [1, 2, 3, 5, 6, 8, 13, 15, 17, 25, 29])
    self.checkMerge(sol.DoublyLinkedList(1, 5),
                    sol.DoublyLinkedList(2, 6, 7, 8),
                    [1, 2, 5, 6, 7, 8])
    self.checkMerge(sol.DoublyLinkedList(1, 5, 7, 9),
                    sol.DoublyLinkedList(2, 4),
                    [1, 2, 4, 5, 7, 9])

  def checkSort(self, n):
    s = sol.DoublyLinkedList()
    for e in random.sample(range(1000000), n):
      s.append(e)
    t0 = time.perf_counter()
    s.sort()
    t1 = time.perf_counter()
    self.assertEqual(len(s), n)
    self.consistency(s)
    p = s.first()
    while p.next is not s.last():
      self.assertLessEqual(p.el, p.next.el)
      p = p.next
    #print("Sorting %d items took %g milliseconds" % (n, 1000*(t1-t0)))
    
  def test_sort(self):
    for n in 10, 100, 1000, 10000:
      self.checkSort(n)

# --------------------------------------------------------------------
    
if __name__ == '__main__':
  unittest.main(verbosity=2, argv=sys.argv[:1])

# --------------------------------------------------------------------
