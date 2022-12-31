#
# Unit tests for QuickSelect
#

import unittest
import random, sys
if sys.argv[-1] == "solution":
  import solution as sol
else:
  import selection as sol

class TestQuickSelect(unittest.TestCase):

  def check(self, a, k, answer):
    r = sol.quick_select(a, k)
    self.assertEqual(r, answer)

  def test_basic(self):
    a = [ 7 ] * 20
    self.check(a, 0, 7)
    self.check(a, 8, 7)
    self.check(a, 10, 7)
    self.check(a, 19, 7)

  def test_more(self):
    a = [ 1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7 ]
    self.check(a, 2, 2)
    self.check(a, 6, 4)
    self.check(a, 7, 4)
    self.check(a, 8, 4)
    self.check(a, 9, 5)
    self.check(a, 11, 5)

  def test_long(self):
    start = 2367
    step = 7
    for n in [ 100, 3000, 100000 ]: 
      a = list(range(start, start + step * n, step))
      random.shuffle(a)
      for i in range(30):
        k = random.randrange(len(a))
      self.check(a, k, start + step * k)

# --------------------------------------------------------------------
    
if __name__ == '__main__':
  unittest.main(verbosity=2, argv=sys.argv[:1])

# --------------------------------------------------------------------
