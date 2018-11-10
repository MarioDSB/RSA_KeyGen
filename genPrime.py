import sys
import random
from datetime import datetime


max_rounds = 10
smallPrimes = []
e = 65537


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

    for w in range(rounds):
        a = random.randint(2, n-2)
        b = pow(a, d, n)
        if b == 1 or b == n - 1:
            return True
        for i in range(r-1):
            b = pow(b, 2, n)
            if b == n-1:
                break

        return False

    return True


def fermat_lt(n, rounds):

    for w in range(rounds):
        a = random.randint(2, n-2)
        b = pow(a, (n-1), n)
        if b != 1:
            return False

    return True


def fermat_test(n):
    while not fermat_lt(n, max_rounds):
        n = gen_rand(int(sys.argv[1]))

        while any(n % i == 0 and n != i for i in smallPrimes):
            n = gen_rand(int(sys.argv[1]))

    return n


def miller_rabin_test(n):
    while not miller_rabin_pt(n, max_rounds):
        n = gen_rand(int(sys.argv[1]))

        # We have to recheck all the previous conditions after generating a new number
        while any(n % i == 0 and n != i for i in smallPrimes):
            n = gen_rand(int(sys.argv[1]))

        n = fermat_test(n)

    return n


def generate_prime(n):
    while not miller_rabin_pt(2*n + 1, max_rounds) and not miller_rabin_pt(n, max_rounds):
        n = gen_rand(int(sys.argv[1]))

        # Using sieve of Erasthotens to eliminate numbers that are divisible by the first X known primes.
        while any(n % i == 0 and n != i for i in smallPrimes):
            n = gen_rand(int(sys.argv[1]))

        # If the number passed the previously (very) naive test, do checks with Fermat's little theorem.
        n = fermat_test(n)

        # If we've got a survivor here (highly unlikely), perform the more computationally complex miller-rabin test.
        n = miller_rabin_test(n)

        break

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

    p = gen_rand(int(sys.argv[1]))
    q = gen_rand(int(sys.argv[1]))

    smallPrimes = er_sieve(e)

    p = generate_prime(p)
    q = generate_prime(q)

    while not gcd(e, (p-1)*(q-1)) == 1:
        p = generate_prime(p)
        q = generate_prime(q)

    # We need to calculate d (using Extended Euclid)
    print(p*q, p, q, e, )
    print("")

    # No need to use this timer. We can just run "time python genPrime 4096"
    t = datetime.now() - startTime
    print(t)