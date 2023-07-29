import sys
import math

while True:
    l=0
    mi=0
    
    for i in range(8):
        mountain_h = int(input())
        if l < mountain_h :
            l = mountain_h
            mi= i
    print (mi)
        