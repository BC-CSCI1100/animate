# Animation Library
#
# A Model-View-Update animation library for Python.
# Bob Muller
#
# A simple circle example.
#
# run: python3 polygon.py
#
# NB: The animate.py file should be in Python site-packages directory
# or in PYTHONPATH.

import math
from animate import *

def polygon(side, color):
  a = side / 2.0
  b = math.sqrt(side ** 2.0 - a ** 2.0)
  (x1, y1) = (a, -b)
  (x2, y2) = (side, 0)
  (x3, y3) = (a, b)
  (x4, y4) = (-a, b)
  (x5, y5) = (-side, 0)
  dxys = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]
  return Image.polygon(dxys, color)

def draw(_):
  side = 200
  shorter = side / 2
  longer = math.sqrt(side ** 2.0 - shorter ** 2.0)
  box = Image.rectangle(2 * side, 2 * longer, Color.Red, lineWidth=1)
  poly = polygon(200, Color.DodgerBlue)
  boxedPoly = Image.placeImage(poly, (0, 0), box)
  pin = Image.circle(4, Color.Red)
  backing = Image.empty(800, 800, Color.LightGray)
  backedBoxedPoly = Image.placeImage(boxedPoly, (200, 200), backing)
  return Image.placeImage(pin, (198, 198), backedBoxedPoly)

Animate.start(viewLast=draw)
