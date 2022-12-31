#
# Unit tests for listset
#

import unittest
import listset as sol
#import solution as sol

# --------------------------------------------------------------------

class TestListSet(unittest.TestCase):

  def assertSet(self, s, els):
    s1 = set()
    for e in s:
      s1.add(e)
    self.assertEqual(len(s), len(s1))
    self.assertEqual(s1, set(els))
    
  def test_basic(self):
    a = sol.set(range(1, 11))
    self.assertEqual(str(a), "ListSet(1,2,3,4,5,6,7,8,9,10)")
    self.assertEqual(len(a), 10)
    a.add(13)
    a.remove(5)
    a.discard(15)
    self.assertEqual(len(a), 10)
    self.assertSet(a, [1,2,3,4,6,7,8,9,10,13])

  def test_union(self):
    a = sol.set(range(1, 11))
    b = sol.set(range(1, 21))
    c = a.union(set([17, 19]))
    self.assertSet(c, [1,2,3,4,5,6,7,8,9,10,17,19])
    self.assertSet(a, range(1, 11))
    self.assertEqual(len(b), 20)
    self.assertTrue(a.issubset(b))
    self.assertFalse(c.issuperset(b))
    self.assertTrue(b.issuperset(c))
    self.assertTrue(a.issubset(c))
    
  def test_difference1(self):
    a = sol.set(range(1, 11))
    b = sol.set(range(1, 21, 2))
    d1 = b.difference(a)
    self.assertEqual(d1, [11,13,15,17,19])
    self.assertSet(b, range(1, 21, 2))
    d2 = a.difference(b)
    self.assertEqual(d2, [2,4,6,8,10])
    self.assertSet(a, range(1, 11))
    
  def test_difference2(self):
    a = sol.set(range(100, 201))
    b = sol.set(range(50, 251))
    d1 = b.difference(a)
    self.assertSet(d1, list(range(50,100)) + list(range(201, 251)))
    self.assertSet(b, range(50, 251))
    d2 = a.difference(b)
    self.assertSet(d2, [])
    self.assertSet(a, range(100, 201))
    
  def test_difference2(self):
    a = sol.set(range(100, 201))
    b = sol.set(range(500, 551))
    d1 = b.difference(a)
    self.assertSet(d1, range(500, 551))
    self.assertSet(b, range(500, 551))
    d2 = a.difference(b)
    self.assertSet(d2, range(100, 201))
    self.assertSet(a, range(100, 201))

  def test_intersection1(self):
    a = sol.set(range(0, 51, 5)) # 0, 5, 10, 15, ... 50
    b = sol.set(range(0, 61, 3)) # 0, 3, 6, 9, ... 60
    d1 = a.intersection(b)
    self.assertSet(d1, [0, 15, 30, 45])
    self.assertSet(a, range(0, 51, 5))
    d2 = b.intersection(a)
    self.assertSet(d2, [0, 15, 30, 45])
    self.assertSet(b, range(0, 61, 3))    
    
  def test_intersection2(self):
    a = sol.set(range(8, 101, 8)) # 8, 16, 24, ...
    b = sol.set(range(0, 144, 2)) # 0, 2, 4, 6, ... 
    d1 = a.intersection(b)
    self.assertSet(d1, range(8, 101, 8))
    self.assertSet(a, range(8, 101, 8))

  def test_intersection2(self):
    a = sol.set([8, 16, 32, 40, 56, 64, 80])
    b = sol.set(range(0, 144, 3)) # 0, 3, 6, ... 141
    d1 = a.intersection(b)
    self.assertSet(d1, [])

# --------------------------------------------------------------------

if __name__ == '__main__':
  unittest.main()

# --------------------------------------------------------------------
