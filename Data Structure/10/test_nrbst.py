#
# Unit tests for Non-Recursive BST
#

import unittest
import sys, random
if sys.argv[-1] == "solution":
  import solution as sol
else:
  import nrbst as sol
import bst   # for comparison

# --------------------------------------------------------------------

# Make testing deterministic
random.seed("nrbst seed")

# --------------------------------------------------------------------

class TestNonRecursiveBST(unittest.TestCase):

  def test_insertions(self):
    t = sol.dict()
    ref = bst.dict()
    for i in range(100):
      k = random.randrange(10000)
      t[k] = "Test"
      ref[k] = "Test"
      self.assertEqual(str(t), str(ref))

  def test_deletions(self):
    t = sol.dict()
    ref = bst.dict()
    for k in [13, 29, 17, -12, -13, 29, 99, 100, 17, 12, -100, 200, 157,
              301, 75, 64, 89, -29, -75, 160, 170, 290, 270, -301, -200,
              -65, -170, -99, -157 ]:
      if k > 0:
        t[k] = "Test"
        ref[k] = "Test"
      else:
        del t[-k]
        del ref[-k]
      self.assertEqual(str(t), str(ref))
        
  def test_all(self):
    t = sol.dict()
    ref = bst.dict()
    els = set() # keep set of elements in treeN
    for i in range(1000):
      k = random.randrange(-3000 if i > 10 else 0, 10000)
      if k > 0:
        t[k] = "Test"
        ref[k] = "Test"
        els.add(k)
      else:
        if (k % 10) == 0:   # test some keys not in tree
          key = -k
        else:
          key = random.choice(list(els))
        del t[key]
        del ref[key]
        els.discard(key)
      self.assertEqual(str(t), str(ref))
        
# --------------------------------------------------------------------
    
if __name__ == '__main__':
  unittest.main(verbosity=2, argv=sys.argv[:1])

# --------------------------------------------------------------------
