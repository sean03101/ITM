#
# Unit tests for Immutable BST
#

import unittest
import sys, random, time
if sys.argv[-1] == "solution":
  import solution as sol
else:
  import ibst as sol
import bst   # for comparison

# --------------------------------------------------------------------

# Make testing deterministic
random.seed("ibst seed")

# --------------------------------------------------------------------

class TestImmutableBST(unittest.TestCase):

  def test_a_insertions(self):
    t = sol.Set()
    ref = bst.dict()
    for i in range(100):
      k = random.randrange(10000)
      t1 = t + k
      self.assertEqual(str(t), str(ref)) # t has not changed!
      ref[k] = "Test"
      self.assertEqual(str(t1), str(ref)) # t1 is equal to new tree
      t = t1

  def test_b_deletions(self):
    t = sol.Set()
    ref = bst.dict()
    for k in [13, 29, 17, -12, -13, 29, 99, 100, 17, 12, -100, 200, 157,
              301, 75, 64, 89, -29, -75, 160, 170, 290, 270, -301, -200,
              -65, -170, -99, -157 ]:
      if k > 0:
        t1 = t + k
        self.assertEqual(str(t), str(ref)) # t has not changed!
        ref[k] = "Test"
      else:
        t1 = t - (-k)
        self.assertEqual(str(t), str(ref)) # t has not changed!
        del ref[-k]
      self.assertEqual(str(t1), str(ref))
      t = t1
        
  def test_c_all(self):
    t = sol.Set()
    ref = bst.dict()
    els = set()
    for i in range(1000):
      k = random.randrange(-3000 if i > 10 else 0, 10000)
      if k > 0:
        t1 = t + k
        self.assertEqual(str(t), str(ref)) # t has not changed!
        ref[k] = "Test"
        els.add(k)
      else:
        if (k % 10) == 0:   # test some keys not in tree
          key = -k
        else:
          key = random.choice(list(els))
        t1 = t - key
        self.assertEqual(str(t), str(ref)) # t has not changed!
        del ref[key]
        els.discard(key)
      self.assertEqual(str(t1), str(ref))
      t = t1

  def test_d_upper_neighbor(self):
    t = sol.Set()
    els = set()
    for i in range(1000):
      k = random.randrange(100000)
      t = t + k
      els.add(k)
    els = list(els)
    els.sort()
    un = t.upper_neighbor(els[0] - 17)
    self.assertEqual(un, els[0])
    for i in range(len(els) - 1):
      un = t.upper_neighbor(els[i])
      self.assertEqual(un, els[i+1])
      un = t.upper_neighbor(0.5 * (els[i] + els[i+1]))
      self.assertEqual(un, els[i+1])
    with self.assertRaises(KeyError):
      un = t.upper_neighbor(els[-1])
    with self.assertRaises(KeyError):
      un = t.upper_neighbor(els[-1] + 17)

  def checkRange(self, t, els, low, high, answer):
    r = t.range(low, high)
    self.assertEqual(r, answer)

  def test_e_range(self):
    t = sol.Set()
    els = set()
    for i in range(1000):
      k = random.randrange(100000)
      t = t + k
      els.add(k)
    els = list(els)
    els.sort()
    for i in range(100):
      lowi = random.randrange(0, len(els)-5)
      highi = random.randrange(lowi, len(els))
      self.checkRange(t, els, els[lowi], els[highi], els[lowi:highi])
      self.checkRange(t, els, els[lowi]-0.4, els[highi], els[lowi:highi])
      self.checkRange(t, els, els[lowi]-0.4, els[highi]+0.4, els[lowi:highi+1])
      self.checkRange(t, els, els[lowi]-0.4, els[lowi]+0.4, els[lowi:lowi+1])
      self.checkRange(t, els, els[lowi]-0.4, els[lowi]-0.2, [])
    self.checkRange(t, els, els[0]-17, els[0], [])
    self.checkRange(t, els, els[0]-17, els[0]-13, [])    
    self.checkRange(t, els, els[0]-17, els[1], els[0:1])
    self.checkRange(t, els, els[0]-17, els[2], els[0:2])
    self.checkRange(t, els, els[0]-17, els[10]+0.4, els[0:11])
    self.checkRange(t, els, els[-1], els[-1] + 17, els[-1:])
    self.checkRange(t, els, els[-1]-0.4, els[-1] + 17, els[-1:])
    self.checkRange(t, els, els[-5]-0.4, els[-1] + 17, els[-5:])

  def checkEls(self, t, els):
    if len(els) == 0:
      self.assertTrue(t.is_empty())
    else:
      m0 = t.min()
      m1 = t.max()
      r = t.range(m0, m1+1)
      self.assertEqual(r, els)

  def checkSplit(self, t, tref, els, i):
    t1, t2 = t.split(els[i])
    self.assertEqual(str(t), tref, msg="Split changed original tree!")
    self.checkEls(t1, els[:i+1])
    self.checkEls(t2, els[i+1:])
    
  def test_f_split(self):
    t = sol.Set()
    els = set()
    for i in range(1000):
      k = random.randrange(100000)
      t = t + k
      els.add(k)
    els = list(els)
    els.sort()
    tref = str(t)
    self.checkSplit(t, tref, els, 0)
    self.checkSplit(t, tref, els, len(els)-1)
    for i in range(100):
      k = random.randrange(len(els))
      self.checkSplit(t, tref, els, k)

  def test_g_split_time(self):
    t = sol.Set()
    for i in range(100000):
      k = random.randrange(100000)
      t = t + k
    t0 = time.perf_counter()
    r1, r2 = t.split(50000)
    t1 = time.perf_counter()
    self.assertLessEqual(r1.max(), 50000)
    self.assertGreater(r2.min(), 50000)
    self.assertLess(t1 - t0, 0.01,
                    msg="Your Split does not seem to run in O(h) time.")
      
# --------------------------------------------------------------------
    
if __name__ == '__main__':
  unittest.main(verbosity=2, argv=sys.argv[:1])

# --------------------------------------------------------------------
