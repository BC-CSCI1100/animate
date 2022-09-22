# Animation Library
#
# A Model-View-Update animation library for Python.
# Bob Muller
#
# A simple bounding box example.
#
# run: python3 boundingBox.py
#
# NB: The animate.py file should be in Python site-packages directory
# or in PYTHONPATH.

from animate import *

# draw : unit -> image
#
def draw(_):
  backing   = Image.empty(800, 800, Color.LightGray)
  bounding  = Image.rectangle(400, 400, Color.Red, lineWidth=1)
  boundBack = Image.placeImage(bounding, (200, 200), backing)
  circle    = Image.circle(200, Color.DodgerBlue)
  placed    = Image.placeImage(circle, (200, 200), boundBack)
  pin       = Image.circle(5, Color.Red)
  return Image.placeImage(pin, (198, 198), placed)

Animate.start(viewLast=draw)
