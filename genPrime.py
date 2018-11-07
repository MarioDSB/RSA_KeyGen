import os
import sys
import random

def genRand(l):
  n=0
  w = int(l/2)

  p = [0]*w

  # It's rather important to pay attention to what you're doing, since urandom returns a sequence of n BYTES...
  bitseq = os.urandom(int(w/8))

  for i in range(0,len(bitseq)):
    b = format(bitseq[i],'08b')
    print(b,i)
    for j in range(0,len(b)):
      p[i] = int(b[j])

  p[0] = 1
  p[w-1] = 1

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
