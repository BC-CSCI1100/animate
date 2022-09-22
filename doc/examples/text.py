# Animation Library
#
# A Model-View-Update animation library for Python.
# Bob Muller
#
# A simple circle example.
#
# run: python3 text.py
#
# NB: The animate.py file should be in Python site-packages directory
# or in PYTHONPATH.

from animate import *

def draw(_):
  backing = Image.rectangle(800, 800, Color.Red)
  text = Image.text("Four score and seven years ...", Color.White, size=200)
  return Image.placeImage(text, (0, 0), backing)

Animate.start(viewLast=draw)
