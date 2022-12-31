# Show image using Tkinter
# PIL Docs: http://effbot.org/imagingbook/imagedraw.htm
# Need python3-pil and python3-pil.imagetk

import tkinter as _Tkinter
from PIL import ImageTk as _ImageTk
from PIL import Image as _Image
from PIL import ImageDraw as _ImageDraw
import sys as _sys

_root = None
_image = None
_title = None
_label = None

# --------------------------------------------------------------------

def _window_closed():
  _root.destroy()
  _sys.exit(9)

def new_canvas(width, height, color, title = "CS206"):
  global _image
  global _title
  assert(_image is None)
  _title = title
  _image = _Image.new("RGB", (width, height), color)
  return _ImageDraw.Draw(_image)
  
def show(ms = None):
  global _root
  global _label
  global _image
  assert(_image is not None)
  if _root is None:
    _root = _Tkinter.Tk()
    _root.geometry('%dx%d' % _image.size)
    _root.title(_title)
    _root.bind("<Button>", lambda x: _root.quit())
    _root.bind("<Return>", lambda x: _root.quit())
    _root.protocol("WM_DELETE_WINDOW", _window_closed)
  tkpi = _ImageTk.PhotoImage(_image)
  if _label is None:
    _label = _Tkinter.Label(_root, image=tkpi)
    _label.place(x=0, y=0, width=_image.size[0], height=_image.size[1])
  else:
    _label.config(image=tkpi)
  if ms is not None:
    _root.after(ms, lambda : _root.quit())
  _root.mainloop() # wait until timeout or user clicks the window

def save(fn):
  assert(_image is not None)
  _image.save(fn)

# --------------------------------------------------------------------
