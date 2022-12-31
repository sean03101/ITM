#
# Unit tests for Morse decoder
#

import unittest
import sys
if sys.argv[-1] == "solution":
  import solution as sol
else:
  import morse as sol

class TestMorse(unittest.TestCase):

  def check(self, morse, ref):
    answer = sol.morse_table.decode(morse)
    self.assertEqual(answer, ref)

  def test_letters(self):
    morse_list = ['.-','-...','-.-.','-..','.','..-.','--.',
                  '....','..','.---','-.-','.-..','--','-.',
                  '---','.--.','--.-','.-.','...','-','..-',
                  '...-','.--','-..-','-.--','--..']
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z']

    for x in range(len(morse_list)):
      self.check(morse_list[x], alphabet[x])

  def test_digits(self):
    morse_list = ['.----','..---','...--','....-','.....',
                   '-....','--...','---..','----.','-----']
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for x in range(len(morse_list)):
      self.check(morse_list[x], digits[x])

      
# --------------------------------------------------------------------
    
if __name__ == '__main__':
  unittest.main(verbosity=2, argv=sys.argv[:1])

# --------------------------------------------------------------------
