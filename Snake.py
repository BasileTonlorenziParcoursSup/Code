from math import *
from cmath import *
from matplotlib.pyplot import *
from random import *
from kandinsky import *
from ion import *
from time import *

v = 0
x = 165
y = 120
couleur = color(50,50,50)
#d definie la direction
d = 0
longueur = []
t = 5
f = 0.2

fill_rect(0,0,320,10,couleur)
fill_rect(0,0,10,255,couleur)
fill_rect(315,0,10,255,couleur)
fill_rect(0,220,320,10,couleur)

def carre(x,y):
  fill_rect(x,y,10,10,couleur)
  longueur.append(x)
  longueur.append(y)

def carre_blanc(a,b):
  fill_rect(a,b,10,10,color(255,255,255))

def boost():
  g = randint(2,27)*10+5
  h = randint(2,20)*10
  while get_pixel(g,h) == couleur:
    g = randint(3,27)*10+5
    h = randint(3,20)*10
  fill_rect(g,h,10,10,color(255,0,0))
boost()
longueur.clear()

while v == 0:
  sleep(f)
  if d == 0:
    if get_pixel(x+10,y) == couleur:
      v = 1
    if get_pixel(x+10,y) == color(255,0,0):
      f = f/1.05
      t += 2
      boost()
    x+=10
    carre(x,y)
  elif d == 1:
    if get_pixel(x,y+10) == couleur:
      v = 1
    if get_pixel(x,y+10) == color(255,0,0):
      f = f/1.05
      t += 2
      boost()
    y+=10
    carre(x,y)
  elif d == 2:
    if get_pixel(x-10,y) == couleur:
      v = 1
    if get_pixel(x-10,y) == color(255,0,0):
      f = f/1.05
      t += 2
      boost()
    x-=10
    carre(x,y)
  else:
    if get_pixel(x,y-10) == couleur:
      v = 1
    if get_pixel(x,y-10) == color(255,0,0):
      f = f/1.05
      t += 2
      boost()
    y-=10
    carre(x,y)
  if keydown(KEY_UP) == True:
    if d != 1:
      d = 3
  elif keydown(KEY_LEFT) == True:
    if d != 0:
      d = 2
  elif keydown(KEY_DOWN) == True:
    if d != 3:
      d = 1
  elif keydown(KEY_RIGHT) == True:
    if d != 2:
      d = 0
  if len(longueur) >= t:
    carre_blanc(longueur[0],longueur[1])
    longueur.reverse()
    longueur.pop()
    longueur.pop()
    longueur.reverse()

draw_string("t'as perdu'",80,90)
draw_string("ta taille",100,120)
t = str((t-1)/2)
draw_string(t,100,150)
