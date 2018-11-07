import sys
import random
from datetime import datetime

# Generate a random number n such that 
def genRand(l):
  n=0
  w = int(l/2)

  n = 0

  while (n % 2 == 0):
    n = random.randrange(1 << w-1, 1 << w)

  return n

# Sieve of erasthotens for the generation of the small primes up to s
def er_sieve(s):
  sis = [True]*(s+1)
  
  sis[0] = False
  sis[1] = False
  p = 2

  while ((p**2) <= s):
    if (sis[p]):
      for i in range(p*2,s+1,p):
        sis[i]=False
    p += 1
  
  primes=[]

  for j in range(2,s):
    if (sis[j]):
      primes.append(j)

  return primes


def mrab_pr(n, k):

  d = n - 1
  r = 0

  while (d % 2 == 0):
    d >>= 1
    r += 1

  for w in range(k):
    a = random.randint(2,n-2)
    b = pow(a,d,n)
    if (b == 1 or b == n - 1):
      return True
    for i in range(r-1):
      b = pow(b,2,n)
      if (b == n-1):
        break
    
    return False

  return True

def ferm_pr(n, k):
  
  for w in range(k):
    a = random.randint(2,n-2)
    b = pow(a,(n-1),n)
    if (b != 1):
      return False
      
  return True

if __name__ == "__main__":

  startTime = datetime.now()

  p = genRand(int(sys.argv[1]))
  q = genRand(int(sys.argv[1]))

  smallPrimes = er_sieve(65537)

  # TODO: fixme make this loop less loopy (if you know what I mean); this code is UGLY.

  while (True):
    p = genRand(int(sys.argv[1]))
    
    # Using sieve of erasthotens to eliminate numbers that are divisible by the first 5000 known primes.
    while (any( p % i == 0 for i in smallPrimes)):
      p = genRand(int(sys.argv[1]))

    # If the number passed the previously (very) naive test, then do checks with Fermat's little theorem.
    while (not ferm_pr(p,10)):
      p = genRand(int(sys.argv[1]))
      while (any( p % i == 0 for i in smallPrimes)):
        p = genRand(int(sys.argv[1]))
    
    # If we've got a survivor here (highly unlikely), perform the more computationally complex miller-rabin test.
    while (not mrab_pr(p,10)):
      p = genRand(int(sys.argv[1]))
      # Sadly we have to recheck all the previous conditions after generating a new number...
      while (any( p % i == 0 for i in smallPrimes)):
        p = genRand(int(sys.argv[1]))
      
      while (not ferm_pr(p,10)):
        p = genRand(int(sys.argv[1]))
        while (any( p % i == 0 for i in smallPrimes)):
          p = genRand(int(sys.argv[1]))
    
    break

  while (True):
    q = genRand(int(sys.argv[1]))
    
    # Using sieve of erasthotens to eliminate numbers that are divisible by the first 5000 known primes.
    while (any( q % i == 0 for i in smallPrimes)):
      q = genRand(int(sys.argv[1]))

    # If the number passed the previously (very) naive test, then do checks with Fermat's little theorem.
    while (not ferm_pr(q,10)):
      q = genRand(int(sys.argv[1]))
      while (any( q % i == 0 for i in smallPrimes)):
        q = genRand(int(sys.argv[1]))
    
    # If we've got a survivor here (highly unlikely), perform the more computationally complex miller-rabin test.
    while (not mrab_pr(q,10)):
      q = genRand(int(sys.argv[1]))
      # Sadly we have to recheck all the previous conditions after generating a new number...
      while (any( q % i == 0 for i in smallPrimes)):
        q = genRand(int(sys.argv[1]))
      
      while (not ferm_pr(q,10)):
        q = genRand(int(sys.argv[1]))
        while (any( q % i == 0 for i in smallPrimes)):
          q = genRand(int(sys.argv[1]))
    
    break

  print(p)
  print(q)
  print("")
  print(datetime.now() - startTime)