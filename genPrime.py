import os
import sys

def genPrime(l):

  w = int(l/2)

  p = [0]*w

  p[0] = 1
  p[w-1] = 1

  bitseq = os.urandom(w)

  for i in range(1,len(bitseq)-1):
    b = format(bitseq[i],'08b')
    for j in range(0,len(b)):
      p[i] = int(b[j])

  print(p)
  print(len(p))

  n=0

  print(w)

  for k in range(0,w):
    n += ((2**((w-1)-k))*p[k])

  print (n)

  # print(len(p))

  # for i in range(1,w-2):
  #   bitseq = os.urandom(1)
  #   a = int(bitseq[0])
  #   b = format(a,'08b')
  #   for j in range(0,len(b)):
  #     p[i] = (int(b[j]))

  # n = 0

  # for k in range(0,w):
  #   n += (2**k)*p[k]

if __name__ == "__main__":
    genPrime(int(sys.argv[1]))