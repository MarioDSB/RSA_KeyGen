import sys
import random
from datetime import datetime

l = int(sys.argv[1])

max_rounds = 100
smallPrimes = []
e = 65537
# nsieve such that this sieve will have the first n small primes.
nsieve = 7920


# Generate a random number n such that
# Unnecessary while cycles here, just perform a bitwise OR with 1 on n
def gen_rand(l):
    w = int(l/2)

    min = (1 << (w-1)) | 1
    max = (1 << (w)) - 1

    n = random.randrange(min, max) | 1

    return n


# Sieve of Erasthotens for the generation of the small primes up to s
def er_sieve(s):
    sis = [True]*(s+1)

    sis[0] = False
    sis[1] = False
    p = 2

    while (p**2) <= s:
        if sis[p]:
            for i in range(p*2, s+1, p):
                sis[i] = False
        p += 1

    primes = []

    for j in range(2, s):
        if sis[j]:
            primes.append(j)

    return primes


def miller_rabin_pt(n, rounds):

    d = n - 1
    r = 0

    while d % 2 == 0:
        d >>= 1
        r += 1

    for _ in range(rounds):
        a = random.randint(2, n-2)
        b = pow(a, d, n)
        if b == 1 or b == n - 1:
            continue
        for _ in range(r-1):
            b = pow(b, 2, n)
            if b == n-1:
                break
        else:
            return False

    return True


def generate_prime(n):
    while not miller_rabin_pt(n, max_rounds):
        n = gen_rand(l)

        # Using sieve of Erasthotens to eliminate numbers that are divisible by the first X known primes.
        while any(n % i == 0 and n > i for i in smallPrimes):
            n = gen_rand(l)

    return n


def gcd(a, b):
    """
    Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    startTime = datetime.now()

    p = gen_rand(l)
    q = gen_rand(l)

    smallPrimes = er_sieve(nsieve)

    p = generate_prime(p)
    q = generate_prime(q)

    # p and q can never be ==, factorization would be too easy, i.e. n would be a perfect square.

    n = p*q

    exp = int(l/3)+1

    print (exp)

    print(len(bin(n))-2)


    # Primes are RSA-SAFE if their absolute value is equal or greater than their safe distance.
    # Alternatively, a prime p is a strong prime if (p-1) has a very large prime factor
    # Source: https://eprint.iacr.org/2009/318.pdf
    # Source: https://crypto.stackexchange.com/questions/5262/rsa-and-prime-difference
    safedist = pow(2,exp)

    print(safedist)

    while p == q or abs(p-q) < safedist:
        q = generate_prime(l)

    while not gcd(e, (p-1)*(q-1)) == 1:
        p = generate_prime(p)
        q = generate_prime(q)

    #print(abs(p-q) >= safedist)

    #print (p)
    #print ("")
    #print (q)

    # We need to calculate d (using Extended Euclid)
    #print(p*q, p, q, e, )
    #print("")

    # No need to use this timer. We can just run "time python genPrime 4096"
    t = datetime.now() - startTime
    print(t)