#
# A field for playing MineSweeper
# Using one list for the 2-dimensional field

import random

class Field():
  def __init__(self, nrows, ncols, nbombs):
    self._nrows = nrows
    self._ncols = ncols
    self._field = [ '.' ] * (nrows * ncols)
    # now distribute the bombs
    self._bombs = set()
    while len(self._bombs) < nbombs:
      row, col = random.randrange(nrows), random.randrange(ncols)
      self._bombs.add((row, col))

  def rows(self):
    return self._nrows

  def cols(self):
    return self._ncols

  def cell(self, row, col):
    """Returns contents of cell (row, col). 
 '.' means still invisible,
 '#' means invisible and marked,
 ' ' means no bomb in neighborhood, already visible,
 '1' to '8' means number of bombs in neighborhood, already visible.
 It's okay for (row, col) to be outside the field."""
    if 0 <= row < self._nrows and 0 <= col < self._ncols:
      return self._field[row * self._ncols + col]
    else:
      return '.'

  def _set_cell(self, row, col, el):
    self._field[row * self._ncols + col] = el

  def _count_bombs(self, row, col):
    """Return number of bombs in the neighborhood of cell (row, col)"""
    count = 0
    for i in range(-1, 2):
      for j in range(-1, 2):
        if (i != 0 or j != 0) and ((row + i, col + j) in self._bombs):
          count += 1
    return count

  def display(self, show_bombs = False):
    """Display the field.  Display all bombs if show_bombs is true."""
    print("                    ", end='')
    for col in range(10, self._ncols + 1):
      print(col//10, end=' ')
    print()
    print("  ", end='')
    for col in range(1, self._ncols + 1):
      print(col % 10, end=' ')
    print()
    for row in range(self._nrows):
      print(chr(row + ord('A')), end=' ')
      for col in range(self._ncols):
        if show_bombs and (row, col) in self._bombs:
          print('*', end=' ')
        else:
          print(self.cell(row, col), end=' ')
      print()
    print()

  def uncover(self, row, col):
    "Uncover the cell (row, col).  Returns True if there is a bomb!"
    if (row, col) in self._bombs:
      return True
    if self.cell(row, col) == '.':
      b = self._count_bombs(row, col)
      if b == 0:
        self._set_cell(row, col, ' ')
      else:
        self._set_cell(row, col, "%d" % b)

  def mark(self, row, col):
    "Mark the cell (row, col)."
    assert self.cell(row, col) in '.#', "Cell is already visible!"
    if self.cell(row, col) == '#':
      self._set_cell(row, col, '.') # unmark
    else:
      self._set_cell(row, col, '#') # mark

  def all_visible(self):
    for row in range(self._nrows):
      for col in range(self._ncols):
        if self.cell(row, col) == '.':
          return False
    return True

  def num_marks(self):
    count = 0
    for row in range(self._nrows):
      for col in range(self._ncols):
        if self.cell(row, col) == '#':
          count += 1
    return count
