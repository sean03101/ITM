#
# Play MineSweeper

import sys
from field1 import Field

def get_response(nrows, ncols): 
  "Returns (t, row, col), where t is True if we want to mark the cell."
  while True:
    mark = False
    l = input("What cell do you want to check? ").upper()
    if l.startswith('#'):
      mark = True
      l = l[1:]
    if len(l) >= 2:
      srow = l[0]
      scol = l[1:]
      if 'A' <= srow < chr(ord('A') + nrows):
        row = ord(srow) - ord('A')
        try:
          col = int(scol)
          if 1 <= col <= ncols:
            return (mark, row, col-1)
        except ValueError:
          pass # okay, continue trying
    print("I don't understand!")

def minesweeper(nrows, ncols, nbombs):
  f = Field(nrows, ncols, nbombs)
  while True:
    f.display()
    if f.all_visible() and f.num_marks() == nbombs:
      print("Congratulations, you solved it!")
      f.display(True)
      return 1
    mark, row, col = get_response(nrows, ncols)
    if mark:
      if f.cell(row, col) not in ".#":
        print("Cannot mark visible or marked cell")
      else:
        f.mark(row, col)
    else:
      if f.uncover(row, col):
        print("Boom Boom Boom")
        print("You are dead!")
        f.display(True)
        return -1

if len(sys.argv) != 4:
  print("Usage: python minesweeper <nrows> <ncols> <nbombs>")
else:
  minesweeper(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

