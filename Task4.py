#!/usr/bin/env python3

######## ЗАДАНИЕ (4) ########
chislo = int(input("Введите число "))
cifra = chislo%10
chislo = chislo//10
while chislo > 0:
  if chislo%10 > cifra:
    cifra = chislo%10
  chislo = chislo//10
print('Наибольшая цифра',cifra)
