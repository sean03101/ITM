#
# Unit tests for recursion exercises
#

import unittest, sys, io
import clockwise
#import clockwise2 as clockwise

# --------------------------------------------------------------------

class MoveFormatException(Exception):
  pass

def run_hanoi(f, n):
  out = io.StringIO()
  saveOut = sys.stdout
  sys.stdout = out
  try:
    f(n, 'A', 'B', 'C')
  finally:
    sys.stdout = saveOut
  moves = []
  for l in out.getvalue().splitlines():
    f = l.strip().split()
    if f == []: continue
    if (f[0] != "Move" or (f[1] not in ["disk", "disc"]) or
        f[2].rstrip("0123456789") != "" or
        f[3] != "from" or (f[4] not in ["A", "B", "C"]) or
        f[5] != "to" or (f[6] not in ["A", "B", "C"])):
      raise MoveFormatException
    moves.append((int(f[2]), f[4], f[6]))
  return moves

# --------------------------------------------------------------------

class TestThrees(unittest.TestCase):

  def check_moves(self, moves, n):
    poles = { "A": list(range(n, 0, -1)), "B": [], "C": [] }
    for move in moves:
      d, f, t = move
      # check if clockwise move
      self.assertTrue((f + t) in { "AB", "BC", "CA" },
                      "Move from %s to %s" % (f, t))
      # check if disk is the top disk
      self.assertTrue(poles[f][-1] == d) 
      # check if disk is larger than top disk on destination
      self.assertFalse(len(poles[t]) > 0 and poles[t][-1] < d)
      poles[f].pop()
      poles[t].append(d)
    # check that result is what we want
    self.assertEqual(poles["A"], [])
    self.assertEqual(poles["C"], [])
    return len(moves)
    
  def run_cw_hanoi(self, n):
    moves = run_hanoi(clockwise.hanoi_cw, n)
    m = self.check_moves(moves, n)
    print("For %d disks you needed %d moves" % (n, m))
    
  def test_cw(self):
    for n in [1, 2, 3, 4, 7, 10]:
      with self.subTest(i=n):
        self.run_cw_hanoi(n)
    
# --------------------------------------------------------------------

if __name__ == '__main__':
  unittest.main()

# --------------------------------------------------------------------
