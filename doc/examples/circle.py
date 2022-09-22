# Animation Library
#
# A Model-View-Update animation library for Python.
# Bob Muller
#
# A simple circle example.
#
# run: python3 circle.py
#
# NB: The animate.py file should be in Python site-packages directory
# or in PYTHONPATH.

from animate import *

# draw : unit -> image
#
def draw(_):
  return Image.circle(200, Color.DodgerBlue)

Animate.start(viewLast=draw)
