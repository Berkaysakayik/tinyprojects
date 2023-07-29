import sys
import math


xlen = int(input())
x = list(map(int, input().split()))
denişken = 0
sonuc = []

for i in range(xlen):
    denişken = abs (int(x[i]))
    sonuc.append(denişken)

sonuc.sort()

for i in range(xlen):
    if (-int(sonuc[0])) == int(x[i]):
        print(x[i])
        break
    if int(sonuc[0]) == int(x[i]):
        print(sonuc[0])
        break

