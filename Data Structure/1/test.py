#
# Unit tests for recursion exercises
#

import unittest
import recursion
#import solution as recursion

# --------------------------------------------------------------------

class TestThrees(unittest.TestCase):

  def test_threes(self):
    ns = [ 0, 7, 3, 13, 33333, 123454321, 12333983393893 ]
    ans = [ 0, 0, 1, 1, 5, 2, 7 ]
    for i in range(len(ns)):
      with self.subTest(i=i):
        self.assertEqual(recursion.number_of_threes(ns[i]), ans[i], ns[i])

# --------------------------------------------------------------------

class TestPalindrome(unittest.TestCase):

  def test_palindrome(self):
    ns = ["abba", "omma", "a", "", "ere", "era", "amanaplanacanalpanama" ]
    for i in range(len(ns)):
      with self.subTest(i=i):
        self.assertEqual(recursion.palindrome(ns[i]), ns[i] == ns[i][::-1])

# --------------------------------------------------------------------

class TestBinLog(unittest.TestCase):

  def test_binlog(self):
    ns = [7, 8, 17, 1000, 1024, 2500, 1000000, 1000000000]
    ans = [ 2, 3, 4, 9, 10, 11, 19, 29 ]
    for i in range(len(ns)):
      with self.subTest(i=i):
        self.assertEqual(recursion.bin_log(ns[i]), ans[i])

# --------------------------------------------------------------------

if __name__ == '__main__':
  unittest.main()

# --------------------------------------------------------------------
