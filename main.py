"""1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
"""
szám = int(input('Adj meg egy számot! '))

osztás = szám % 2
döntés = szám / 2

if osztás >= 0.1 :
  print ('páratlan')
if döntés <= -1 :
  print ('negatív')


if osztás <= 0.1 :
  print ('páros')
if döntés >= -1 :
  print ('pozitív')