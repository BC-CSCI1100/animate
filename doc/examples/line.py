# Animation Library
#
# A Model-View-Update animation library for Python.
# Bob Muller
#
# A simple circle example.
#
# run: python3 line.py
#
# NB: The animate.py file should be in Python site-packages directory
# or in PYTHONPATH.

from animate import *

# draw : unit -> image
#
def draw(_):
  radius = 200
  circle = Image.circle(radius, Color.White)
  line   = Image.line([(radius, 0), (0, -radius)], Color.Red)
  return Image.placeImage(line, (radius, radius), circle)

Animate.start(viewLast=draw)
