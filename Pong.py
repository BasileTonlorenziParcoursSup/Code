from math import *
from matplotlib.pyplot import *
from kandinsky import *
from random import *
from ion import *
from time import *

#Programme adapter à une calculatrice Numworks
fill_rect(0,0,330,10,color(0,0,0))
fill_rect(0,215,330,15,color(0,0,0))
#a,b = coordonnées de la balle      c,d = mouvement horizontale/verticale
a = 160
b = 125
c = 5
d = 0
v = 0
#xj et x sont les coordonnées des joueurs
x = 0
y = 120
xj = 310
yj = 120
k = 3
ts = 0

aug = 100


def balle(a,b,c,d):
  fill_rect(a-c,b-d,10,10,color(255,255,255))
  fill_rect(a,b,10,10,color(255,0,0))

def joueur(x,y):
  fill_rect(x,y-20,10,20,color(255,255,255))
  fill_rect(x,y+20,10,20,color(255,255,255))
  fill_rect(x,y,10,30,color(255,0,150))

joueur(xj,yj)
joueur(x,y)

while v == 0:
  for i in range(0,3):
    if keydown(KEY_NINE) == True:
      v = 1
    if keydown(KEY_UP) == True and y-5 > 5:
      y -= 5
      joueur(x,y)
    if keydown(KEY_DOWN) == True and y+5 < 200:
      y += 5
      joueur(x,y)
    if keydown(KEY_DIVISION) == True and yj-5 > 5:
      yj -= 5
      joueur(xj,yj)
    if keydown(KEY_MINUS) == True and yj+5 < 200:
      yj += 5
      joueur(xj,yj)
  if xj-10 <= a <= xj and yj <= b <= yj+30:
    c = -c
    d += trunc((b-yj+15)/10)
    k += 1
    a -= 10
    fill_rect(a+10,b,10,10,color(255,255,255))
  if x <= a <= x+10 and y <= b <= y+30:
    c = -c
    d += trunc((b-y+15)/10)
    k += 1
    a += 10
    fill_rect(a-10,b,10,10,color(255,255,255))
  if b+d <= 10:
    d = -d
  if b+d >= 205:
    d = -d
  if a >= 320:
    v = 2
  if a <= 0:
    v = 1
  if k == 5:
    k = 0
    if c <= 0:
      c -= 1
    else:
      c += 1
  a += c
  b += d
  balle(a,b,c,d)

#Les rebonds sont mauvais mais je pense juste m'être trompé sur une valeur
