from math import *
from matplotlib.pyplot import *
from kandinsky import *
from random import *
from time import *
from ion import *

#Fait pour la calculatrice Numworks
x = -2
y = 23
j = 2
v = 0
couleur = color(255,0,0)
grille = []
k = 0

#pour creer les limites horizontales et verticales
for i in range(0,11):
  fill_rect(x,y,7,240,color(0,0,0))
  x += 32
x = 0
y = 219
for i in range(0,11):
  fill_rect(x,y,350,6,color(0,0,0))
  y -= 28
x = 5
y = 0

#Le nom n'est pas très parlant mais cette fonction permet de faire chuté les pièces
def harien(x,k,j,c):
  y = 28
  carre(x,y,c)
  while grille[k+10] == 0 and k < 60:
    sleep(0.3)
    y += 28
    k += 10
    carre(x,y,c)
    carre_blanc(x,y-28)
  carre(x,y,c)
  grille[k] = j

def scan(k,d,f):
  sk = k
  l = 0
  for i in range(0,4):
    if grille[sk] == f:
      sk += d
      l += 1
  if l == 4:
    return True

def victoire(f):
  sk = 0
  for i in range(0,40):
    if scan(sk,10,f) == True:
      return True
    sk += 1
  sk = 0
  for i in range(0,49):
    if sk%10 == 7:
      sk += 3
    if scan(sk,1,f) == True:
      return True
    sk += 1
  sk = 0
  for i in range(0,49):
    if sk%10 == 7:
      sk += 3
    if scan(sk,11,f) == True:
      return True
    sk += 1
  sk = 0
  for i in range(0,49):
    if sk%10 == 0:
      sk += 3
    if scan(sk,9,f) == True:
      return True
    sk += 1

def carre(x,y,c):
  fill_rect(x,y,25,23,c)

def carre_blanc(x,y):
  fill_rect(x,y,25,23,color(255,255,255))

for i in range(0,100):
  grille.append(0)
carre(x,y,couleur)

while v == 0:
  sleep(0.1)
  if keydown(KEY_RIGHT) == True and x+32 < 320:
    x += 32
    carre(x,y,couleur)
    carre_blanc(x-32,y)
    k += 1
  elif keydown(KEY_LEFT) == True and x-30 >= 0:
    x -= 32
    carre(x,y,couleur)
    carre_blanc(x+32,y)
    k -= 1
  if keydown(KEY_OK) == True and j == 2:
    harien(x,k,j,color(255,0,0))
    couleur = color(255,255,0)
    if victoire(2) == True:
      v = 2
    j = 1
    carre(x,y,couleur)
  if keydown(KEY_OK) == True and j == 1:
    harien(x,k,j,color(255,255,0))
    couleur = color(255,0,0)
    if victoire(1) == True:
      v = 1
    j = 2
    carre(x,y,couleur)

if v == 1:
  draw_string("Victoire du jaune",120,15)
else:
  draw_string("Victoire du rouge",120,15)
