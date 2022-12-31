#
# Unit tests for CircularList
#

import unittest
import sys, time
if sys.argv[-1] == "solution":
  import solution as sol
else:
  import circularlist as sol

# --------------------------------------------------------------------

consmsg = "The structure of the circular doubly-linked list is broken."

# --------------------------------------------------------------------

class TestCircularList(unittest.TestCase):

  def make(self, ):
    s = sol.CircularList("CS206")
    for w in [ "is", "a", "lot", "of", "fun",
	       "a", "lot", "of", "fun", "is", "CS206" ]:
      s.append(w)
    return s

  def consistency(self, s):
    p = s.first()
    rear = p.prev
    self.assertIs(rear.next,  p, msg=consmsg)
    while p is not rear:
      self.assertIs(p.next.prev, p, msg=consmsg)
      p = p.next
  
  def test_basic(self):
    s = sol.CircularList("CS206")
    self.assertEqual(str(s), "[CS206]")
    self.consistency(s)
  
  def test_append(self):
    s = self.make()
    self.assertEqual(str(s),
                     "[CS206, is, a, lot, of, fun, a, lot, of, fun, is, CS206]")
    self.consistency(s)

  def test_length(self):
    s = self.make()
    self.assertEqual(len(s), 12)
    self.assertEqual(s.first().el, "CS206")
    self.assertEqual(s.first().prev.el, "CS206")
    s.append("strange")
    self.assertEqual(len(s), 13)

  def test_remove(self):
    s = self.make()
    s.remove(s.first().prev)
    self.consistency(s)
    self.assertEqual(str(s), "[CS206, is, a, lot, of, fun, a, lot, of, fun, is]")
    s.remove(s.first().next.next)
    self.consistency(s)
    self.assertEqual(str(s), "[CS206, is, lot, of, fun, a, lot, of, fun, is]")
    s.remove(s.first().next.next.next.next)
    self.consistency(s)
    self.assertEqual(str(s), "[CS206, is, lot, of, a, lot, of, fun, is]")
    s.remove(s.first().prev)
    self.consistency(s)
    self.assertEqual(str(s), "[CS206, is, lot, of, a, lot, of, fun]")
    s.remove(s.first())
    self.consistency(s)
    self.assertEqual(str(s), "[is, lot, of, a, lot, of, fun]")
    for i in range(1, 6):
      s.remove(s.first())
    self.consistency(s)
    self.assertEqual(str(s), "[of, fun]")
    s.remove(s.first().prev)
    self.consistency(s)
    self.assertEqual(str(s), "[of]")
    self.assertEqual(len(s), 1)
    with self.assertRaisesRegex(ValueError,
                                "Cannot remove only node of a CircularList"):
      s.remove(s.first())
    
  def test_insert(self):
    s = sol.CircularList("A")
    s.insert(s.first(), "B")
    self.consistency(s)
    self.assertEqual(str(s), "[A, B]")
    s.insert(s.first().next, "C")
    self.consistency(s)
    self.assertEqual(str(s), "[A, C, B]")
    s.insert(s.first().prev, "D")
    self.consistency(s)
    self.assertEqual(str(s), "[A, C, D, B]")
    s.insert(s.first().next.next, "E")
    self.consistency(s)
    self.assertEqual(str(s), "[A, C, E, D, B]")

# --------------------------------------------------------------------
    
if __name__ == '__main__':
  unittest.main(verbosity=2, argv=sys.argv[:1])

# --------------------------------------------------------------------
