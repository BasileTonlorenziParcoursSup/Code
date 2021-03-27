from math import *
from matplotlib.pyplot import *
from turtle import *
from random import *
from time import *
from ion import *

#Je precise : les programmes que j'ai fait sont fait pour la calculatrice Numworks
v = 0
x = -120
y = 65
j = 1
pensize(5)
speed(20)
grille = []

#ligne de limite horizontale
penup()
goto(-160,40)
pendown()
goto(160,40)
penup()
goto(-160,-40)
pendown()
goto(160,-40)

#ligne de limite verticale
penup()
goto(-50,120)
pendown()
goto(-50,-120)
penup()
goto(70,120)
pendown()
goto(70,-120)
penup()
speed(10)
k = 0
 #Le découpage est mauvais même pour la calculatrice
def rond(a,b):
  goto(a,b-10)
  pendown()
  circle(20)
  penup()

def croix(c,d):
  pendown()
  goto(c-20,d-20)
  goto(c+20,d+20)
  goto(c,d)
  goto(c+20,d-20)
  goto(c-20,d+20)
  penup()

def scan(k,d,f):
  sk = k
  l = 0
  for i in range(0,3):
    if grille[sk] == f:
      sk += d
      l += 1
  if l == 3:
    return True

def victoire(f):
  sk = 0
  for i in range(0,3):
    if scan(sk,1,f) == True:
      return True
    sk += 3
  sk = 0
  for i in range(0,3):
    if scan(sk,3,f) == True:
      return True
    sk += 1
  for i in range(0,3):
    if scan(sk,3,f) == True:
      return True
    sk += 1
  sk = 0
  if scan(sk,4,f) == True:
    return True
  sk = 2
  if scan(sk,2,f) == True:
    return True


for i in range(0,25):
  grille.append(0)

while v == 0:
  sleep(0.1)
  if keydown(KEY_RIGHT) == True and x+110 < 160:
    x += 110
    k += 1
  elif keydown(KEY_UP) == True and y+70 < 130:
    y += 70
    k -= 3
  if keydown(KEY_LEFT) == True and x-110 > -160:
    x -= 110
    k -= 1
  elif keydown(KEY_DOWN) == True and y-70 > -130:
    y -= 70
    k += 3
  goto(x,y)
  if keydown(KEY_OK) == True and j == 1 and grille[k] == 0:
    color('red')
    rond(x,y)
    j = 0
    grille[k] = 1
    if victoire(1) == True:
      v = 1
  elif keydown(KEY_OK) == True and j == 0 and grille[k] == 0:
    color('blue')
    croix(x,y)
    j = 1
    grille[k] = 2
    if victoire(2) == True:
      v = 2

reset()
hideturtle()
goto(-60,-20)
if v == 1:
  write("gg le rond")
else:
  write("gg la croix")
