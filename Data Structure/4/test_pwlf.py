#
# Unit tests for PieceWiseLinear
#

import unittest
from pwlf import PieceWiseLinear
#from solution import PieceWiseLinear

# --------------------------------------------------------------------

class TestPWLF(unittest.TestCase):

  def make(self, *xys):
    f = PieceWiseLinear(xys[0], xys[1], xys[2], xys[3])
    i = 4
    while i < len(xys):
      f1 = PieceWiseLinear(xys[i-2], xys[i-1], xys[i], xys[i+1])
      f = f.join(f1)
      i += 2
    return f

  def assertApprox(self, a, b):
    self.assertTrue(abs(a - b) < 1e-13, "%g != %g" % (a, b))
    
  def test_simple(self):
    f = self.make(0, 0, 6, 2)
    self.assertApprox(f(0), 0)
    self.assertApprox(f(6), 2)
    self.assertApprox(f(3), 1)
    self.assertEqual(f.domain(), (0, 6))

  def test_str(self):
    f1 = self.make(0, -3, 5, 2, 6, 2, 9, -7, 13, 5)
    self.assertEqual(str(f1), "(0,-3)..(5,2)..(6,2)..(9,-7)..(13,5)")

  def test_domain(self):
    f1 = self.make(0, 0, 3, 1, 9, 7, 15, 2)
    self.assertEqual(f1.domain(), (0, 15))
    f2 = self.make(0, 0, 6, 2, 8, 5, 13, -5, 20, 51)
    self.assertEqual(f2.domain(), (0, 20))

  def test_call(self):
    f = self.make(0, 0, 6, 2, 8, 5, 13, -5, 20, 51)
    with self.assertRaisesRegex(ValueError, "argument is not in domain"):
      f(-2)
    with self.assertRaisesRegex(ValueError, "argument is not in domain"):
      f(20.5)
    self.assertApprox(f(0), 0)
    self.assertApprox(f(3), 1)
    self.assertApprox(f(7), 3.5)
    self.assertApprox(f(10), 1)
    self.assertApprox(f(19), 43)
    self.assertApprox(f(5), 5/3)    
    self.assertApprox(f(7.5), 4.25)
    self.assertApprox(f(9.5), 2)
    
  def test_join(self):
    f = self.make(0, 1, 3, 7, 4, 3)
    g1 = self.make(5, 3, 8, 8, 10, -4)
    with self.assertRaisesRegex(ValueError, "domains are not contiguous"):
      f.join(g1)
    g2 = self.make(4, 4, 8, 8, 10, -4)
    with self.assertRaisesRegex(ValueError, "discontinuity at connection point"):
      f.join(g2)
    g3 = self.make(4, 3, 8, 8, 10, -4)
    f1 = f.join(g3)
    self.assertEqual(str(f1), "(0,1)..(3,7)..(4,3)..(8,8)..(10,-4)")

  def test_mult(self):
    f = self.make(0, 1, 3, 7, 4, 3)
    g = 3 * f
    self.assertEqual(str(g), "(0,3)..(3,21)..(4,9)")
    self.assertEqual(str(f), "(0,1)..(3,7)..(4,3)")
    
  def test_add_number(self):
    f = self.make(0, 1, 3, 7, 4, 3)
    g1 = f + 3
    self.assertEqual(str(g1), "(0,4)..(3,10)..(4,6)")
    self.assertEqual(str(f), "(0,1)..(3,7)..(4,3)")
    g2 = f - 7
    self.assertEqual(str(g2), "(0,-6)..(3,0)..(4,-4)")
    self.assertEqual(str(f), "(0,1)..(3,7)..(4,3)")    

  def test_add_pwlf(self):
    f = self.make(0, 1, 3, 7, 4, 3)
    g1 = self.make(2, 3, 4, 0)
    h1 = f + g1
    self.assertEqual(str(h1), "(2,8)..(3,8.5)..(4,3)")
    self.assertEqual(str(f), "(0,1)..(3,7)..(4,3)")
    self.assertEqual(str(g1), "(2,3)..(4,0)")
    h1m = f - g1
    self.assertEqual(str(h1m), "(2,2)..(3,5.5)..(4,3)")
    g2 = self.make(4, 8, 5, 9)
    with self.assertRaisesRegex(ValueError, "domains do not overlap"):
      h2 = f + g2
    g3 = self.make(-12, 8, -4, 13, -2, 20, 2, 20, 3.5, 0, 17, 12)
    h3 = f + g3
    self.assertEqual(str(h3),
                     '(0,21)..(2,25)..(3,13.6667)..(3.5,5)..(4,3.44444)')
    g4 = self.make(-12, 8, -4, 13, -2, 20, 2, 20, 3.5, 0)
    h4 = f + g4
    self.assertEqual(str(h4), '(0,21)..(2,25)..(3,13.6667)..(3.5,5)')
    g5 = self.make(-12, 8, -4, 13, -2, 0, 3, 20, 3.5, 0)
    h5 = f + g5
    self.assertEqual(str(h5), '(0,9)..(3,27)..(3.5,5)')
    h6 = f + f
    self.assertEqual(str(h6), '(0,2)..(3,14)..(4,6)')
    g7 = self.make(1, 9, 2, 9)
    h7 = f - g7
    self.assertEqual(str(h7), '(1,-6)..(2,-4)')
      
# --------------------------------------------------------------------

if __name__ == '__main__':
  unittest.main()

# --------------------------------------------------------------------

