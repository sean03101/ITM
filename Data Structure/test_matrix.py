#
# Unit tests for Matrix
#

import unittest
import sys, time, random
if sys.argv[-1] == "solution":
  import solution as sol
else:
  import matrix as sol

# --------------------------------------------------------------------

consmsg = "The structure of the matrix is broken."

# testing is deterministic
random.seed(a="matrix test pattern")

# --------------------------------------------------------------------

def transposed(d):
  dt = {}
  for x, y in d:
    dt[y, x] = d[x, y]
  return dt

def mtimesv(sref, v, nrows):
  result = [0.0] * nrows
  for row, col in sref:
    result[row] += sref[row, col] * v[col]
  return result

def madd(ref1, ref2):
  result = {}
  entries = set(ref1.keys()).union(ref2.keys())
  for x, y in entries:
    v = ref1.get((x, y), 0.0) + ref2.get((x, y), 0.0)
    if v != 0.0:
      result[x, y] = v
  return result
  
# --------------------------------------------------------------------

class TestMatrix(unittest.TestCase):

  def make(self, nrows, ncols, nentries):
    m = sol.Matrix(nrows, ncols)
    ref = {}
    for i in range(nentries):
      row = random.randrange(nrows)
      col = random.randrange(ncols)
      val = random.uniform(-1000000.0, 1000000.0)
      m[row, col] = val
      ref[row, col] = val
    return m, ref

  def consistency(self, s):
    """Checks that data structure is consistent:
Each node appears on the correct row list and the correct column list."""
    nodes = {}  # nodes found on row lists
    for row in range(s.nrows):
      p = s._prow[row]
      while p is not None:
        self.assertEqual(p.row, row, consmsg)
        nodes[p.row, p.col] = p
        if p.right is not None:
          self.assertLess(p.col, p.right.col, consmsg)
        p = p.right
    for col in range(s.ncols):
      p = s._pcol[col]
      while p is not None:
        self.assertEqual(p.col, col, consmsg)
        self.assertIn((p.row, p.col), nodes, consmsg)
        del nodes[p.row, p.col] # remove nodes found on column lists
        if p.down is not None:
          self.assertLess(p.row, p.down.row, consmsg)
        p = p.down
    # check if some row nodes are not in a column list
    self.assertEqual(len(nodes), 0, consmsg)

  def checkMatrix(self, s, ref):
    """Checks that matrix s is identical to reference ref."""
    entries = set()
    for row in range(s.nrows):
      p = s._prow[row]
      while p is not None:
        # 0.0 is not allowed as a node value
        self.assertNotEqual(p.el, 0.0)
        self.assertEqual(p.el, ref[p.row, p.col])
        entries.add((p.row, p.col))
        p = p.right
    self.assertEqual(entries, ref.keys())
  
  def test_basic(self):
    for nrows, ncols, nentries in [(7, 9, 18), (1, 12, 7), (13, 1, 40),
                                   (17, 23, 2), (33, 81, 1), (22, 77, 129),
                                   (10, 10, 100)]:
      s, ref = self.make(nrows, ncols, nentries)
      self.consistency(s)
      self.checkMatrix(s, ref)

  def test_large(self):
    s, ref = self.make(10000, 10000, 30000)
    self.consistency(s)
    self.checkMatrix(s, ref)

  def test_set_item(self):
    s = sol.Matrix(13, 17)
    ref = {}
    self.consistency(s)
    self.checkMatrix(s, ref)
    for x, y, v in [(1, 2, 9), (3, 9, 12), (12, 16, 99),
                    (1, 2, 0), (3, 9, 13), (12, 16, 0),
                    (3, 9, 0)]:
      s[x, y] = v
      if v != 0.0:
        ref[x, y] = v
      else:
        del ref[x,y]
      self.consistency(s)
      self.checkMatrix(s, ref)

  def test_transpose(self):
    for nrows, ncols, nentries in [(7, 9, 18), (1, 12, 7), (13, 1, 40),
                                   (17, 23, 2), (33, 81, 1), (22, 77, 129),
                                   (10, 10, 100), (1000, 1000, 3000)]:
      s, ref = self.make(nrows, ncols, nentries)
      st = s.transposed()
      self.consistency(s)
      self.checkMatrix(s, ref)
      self.consistency(st)
      self.checkMatrix(st, transposed(ref))

  def test_mul(self):
    for nrows, ncols, nentries in [(7, 9, 18), (1, 12, 7), (13, 1, 40),
                                   (17, 23, 2), (33, 81, 1), (22, 77, 129),
                                   (10, 10, 100), (1000, 1000, 3000)]:
      s, ref = self.make(nrows, ncols, nentries)
      for i in range(30):
        v = [ random.uniform(-100.0, 100.0) for x in range(ncols)]
        r = s * v
        rref = mtimesv(ref, v, s.nrows)
        self.consistency(s)
        self.checkMatrix(s, ref)
        for row in range(nrows):
          self.assertAlmostEqual(r[row], rref[row], places=4)

  def test_rmul(self):
    for nrows, ncols, nentries in [(7, 9, 18), (1, 12, 7), (13, 1, 40),
                                   (17, 23, 2), (33, 81, 1), (22, 77, 129),
                                   (10, 10, 100), (1000, 1000, 3000)]:
      s, ref = self.make(nrows, ncols, nentries)
      tref = transposed(ref)
      for i in range(30):
        v = [ random.uniform(-100.0, 100.0) for x in range(nrows)]
        r = v * s
        rref = mtimesv(tref, v, s.ncols)
        self.consistency(s)
        self.checkMatrix(s, ref)
        for col in range(ncols):
          self.assertAlmostEqual(r[col], rref[col], places=4)

  def test_add(self):
    for nrows, ncols, nentries in [(7, 9, 18), (1, 12, 7), (13, 1, 40),
                                   (17, 23, 2), (33, 81, 1), (22, 77, 129),
                                   (10, 10, 100), (1000, 1000, 3000)]:
      s1, ref1 = self.make(nrows, ncols, nentries)
      s2, ref2 = self.make(nrows, ncols, nentries)
      s = s1 + s2
      ref = madd(ref1, ref2)
      self.consistency(s1)
      self.checkMatrix(s1, ref1)
      self.consistency(s2)
      self.checkMatrix(s2, ref2)
      self.consistency(s)
      self.checkMatrix(s, ref)

  def test_add_tozero(self):
    for nrows, ncols, nentries in [(7, 9, 18), (1, 12, 7), (13, 1, 40),
                                   (17, 23, 2), (33, 81, 1), (22, 77, 129)]:
      s1, ref1 = self.make(nrows, ncols, nentries)
      s2, ref2 = self.make(nrows, ncols, 0)
      entries = list(ref1.keys())
      random.shuffle(entries)
      for x, y in entries:
        s2[x, y] = -ref1[x, y]
        ref2[x, y] = -ref1[x, y]
        s = s1 + s2
        ref = madd(ref1, ref2)
        self.consistency(s1)
        self.checkMatrix(s1, ref1)
        self.consistency(s2)
        self.checkMatrix(s2, ref2)
        self.consistency(s)
        self.checkMatrix(s, ref)
        
  def test_transpose_time(self):
    s, ref = self.make(10000, 10000, 30000)
    t0 = time.perf_counter()
    t = s.transposed()
    t1 = time.perf_counter()
    self.consistency(t)
    self.assertLess(t1 - t0, 1.0,
                    msg="Transpose does not seem to run in linear time")

  def test_add_time(self):
    s1, ref1 = self.make(10000, 10000, 30000)
    s2, ref2 = self.make(10000, 10000, 30000)    
    t0 = time.perf_counter()
    t = s1 + s2
    t1 = time.perf_counter()
    self.consistency(t)
    self.assertLess(t1 - t0, 1.0,
                    msg="Addition does not seem to run in linear time")
    
# --------------------------------------------------------------------
    
if __name__ == '__main__':
  unittest.main(verbosity=2, argv=sys.argv[:1])

# --------------------------------------------------------------------
