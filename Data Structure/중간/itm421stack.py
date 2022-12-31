#
# Defines function 'print_stack' that prints out a trace
# of the runtime stack
#

import inspect as _inspect

def print_stack():
  st = _inspect.stack()
  for s in st[1:]:
    locals = s[0].f_locals if s[3] != "<module>" else ""
    print("Function %s: line #%d: %s" % (s[3], s[2], locals))
  
