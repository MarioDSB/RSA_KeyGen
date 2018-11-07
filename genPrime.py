import os
import sys
import random

def genRand(l):
  n=0
  w = int(l/2)

  p = [0]*w
  p[0] = 1
  p[w-1] = 1

  bitseq = os.urandom(w)

  for i in range(1,len(bitseq)-1):
    b = format(bitseq[i],'08b')
    for j in range(0,len(b)):
      p[i] = int(b[j])

  for k in range(0,w):
    n += ((2**((w-1)-k))*p[k])

  return n

def ml_composite(x):

  i = 1
  y = 0

  while (x % (2**i) == 0):
    y = int(x / (2**i))
    i+=1

  i-=1

  print(i, y)

  a = random.randint(1,x)
  print(a)

if __name__ == "__main__":
    x = genRand(int(sys.argv[1]))
    print(x)
    ml_composite(x-1)
