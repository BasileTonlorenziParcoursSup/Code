from math import *
from random import *
from kandinsky import *
 #Programme adapté à la calculatrice Numworks
 #Ce programme est juste esthétique
sx = 160
sy = 110
y = 0
x = 0
up_x = 0
up_y = 0
nb = 0
r = 0
g = 0
b = 0
sr = randint(-1,1)
sg = randint(-1,1)
sb = randint(-1,1)

while True:
  r += sr
  g += sg
  b += sb
  couleur = color(r,g,b)
  x = sx - up_x
  y = sy + up_y
  while x < sx+up_x:
    set_pixel(x,y,couleur)
    x += 1
  while y > sy-up_y:
    set_pixel(x,y,couleur)
    y -= 1
  while x > sx-up_x:
    set_pixel(x,y,couleur)
    x -= 1
  while y < sy+up_y:
    set_pixel(x,y,couleur)
    y += 1
  up_x += 1
  if nb == 2:
    nb = 0
  else:
    up_y += 1
    nb += 1
  if y >= 222:
    sr += randint(-2,2)
    sg += randint(-2,2)
    sb += randint(-2,2)
    up_x = 0
    up_y = 0
