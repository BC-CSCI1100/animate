# CSCI 1100 Gateway to Computer Science

### Fall 2022

---

## Brief Reference for an Animation Library for Python

The animation library is implemented in file **animate.py**. This file is assumed to be in the local python `site-packages` directory or in a directory on the search path `PYTHONPATH`. The animation library depends on Python packages [pygame](https://www.pygame.org/) and [numpy](https://numpy.org/). These packages can be installed using `pip3`.
```bash
pip3 install pygame numpy
```

Import the animation library with `from animate import *`. Then the functions can be referenced as in `Color.make`, `Image.polygon`, `Animate.start` etc.

```python
Color
    make   : red, green, blue, alpha=255 -> color
    random : unit -> color

    red    : color -> int
    green  : color -> int
    blue   : color -> int
    alpha  : color -> int
```
    
```pyton
Image
    circle    : radius, color, lineWidth=0 -> image
    line      : points, color, lineWidth=1 -> image
    polygon   : points, color, lineWidth=0 -> image
    rectangle : width, height, color, lineWidth=0 -> image
    empty     : width, height, color -> image
    text      : string, color, size=FONTSIZE -> image
    
    placeImage  : top, xy, bottom -> image
    placeImages : tops, xys, bottom -> image 
    
  PNGs
    read : path -> image
    show : path -> unit
    dimensions : image -> (width, height)
    toArray    : image -> 2D-array
    fromArray  : 2D-array -> image
```

```python
Animate
  start :
    model=None,
    width=800,
    height=800,
    view=defaultView,               # model -> Image
    tickUpdate=defaultTickUpdate,   # model -> model
    touchUpdate=defaultTouchUpdate, # model * (x * y) * Touch.UP/Touch.Down -> model
    keyUpdate=defaultKeyUpdate,     # model * keyname -> model
    stopWhen=defaultStopWhen,       # model -> boolean
    viewLast=defaultViewLast,       # model -> Image
    -> unit
```
