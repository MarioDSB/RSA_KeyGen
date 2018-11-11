import sys
import random


def genRSAkey(l):
    max_rounds = 100
    e = 65537

    # Generate a random number n such that
    # Unnecessary while cycles here, just perform a bitwise OR with 1 on n
    def gen_rand(l):
        """
        Generate a random number
        :param l: length of the generated number
        :return: the generated number
        """
        w = int(l / 2)

        min = (1 << (w - 1)) | 1
        max = (1 << w) - 1

        n = random.randrange(min, max) | 1

        return n

    def er_sieve(s):
        """
        Application of the Sieve of Erasthotens, for the generation of the small primes up to s
        :param s:
        :return: A list with the generated primes
        """
        sis = [True] * (s + 1)

        sis[0] = False
        sis[1] = False
        p = 2

        while (p ** 2) <= s:
            if sis[p]:
                for i in range(p * 2, s + 1, p):
                    sis[i] = False
            p += 1

        primes = []

        for j in range(2, s):
            if sis[j]:
                primes.append(j)

        return primes

    # nsieve such that this sieve will have the first 1000 small primes.
    # TODO: Find a good reason for considering the first 1000 primes and cite it in our report.
    nsieve = 7920
    small_primes = er_sieve(nsieve)

    def miller_rabin_pt(n, rounds):
        """
        Application of the Miller-Rabin primality test
        :param n: number to test primality
        :param rounds: number of times to perform the algorithm
        :return: True, if number is prime; False, otherwise
        """
        d = n - 1
        r = 0

        while d % 2 == 0:
            d >>= 1
            r += 1

        for _ in range(rounds):
            a = random.randint(2, n - 2)
            b = pow(a, d, n)
            if b == 1 or b == n - 1:
                continue
            for _ in range(r - 1):
                b = pow(b, 2, n)
                if b == n - 1:
                    break
            else:
                return False

        return True

    def generate_prime():
        n = gen_rand(l)

        while not miller_rabin_pt(n, max_rounds):
            n = gen_rand(l)

            # Using sieve of Erasthotens to eliminate numbers that are divisible by the first X known primes.
            while any(n % i == 0 and n > i for i in small_primes):
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

    # eucl_alg & ext_eucl_alg withdrawn from:
    # https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Modular_inverse
    def eucl_alg(a, b):
        """
        Implementation of the Eucledean Algorithm
        a*x + b*y = gcd(x, y)
        :param a:
        :param b:
        :return: (g, x, y), such that a*x + b*y = gcd(x, y)
        """
        if a == 0:
            return b, 0, 1
        else:
            g, x, y = eucl_alg(b % a, a)
            return g, y - (b // a) * x, x

    def ext_eucl_alg(e, phi):
        """
        Implementation of the Extended Eucledean Algorithm, to find out modular inverses
        x = mulinv(b) mod n, (x * b) % n == 1
        :param e:
        :param phi:
        :return:
        """
        g, x, _ = eucl_alg(e, phi)
        if g == 1:
            return x % phi

    p = generate_prime()
    q = generate_prime()

    # p and q can never be equal, factorization would be too easy, i.e. n would be a perfect square.

    exp = int(l / 3) + 1

    # Primes are RSA-SAFE if their absolute value is equal or greater than their safe distance.
    # Alternatively, a prime p is a strong prime if (p-1) has a very large prime factor
    # Source: https://eprint.iacr.org/2009/318.pdf
    # Source: https://crypto.stackexchange.com/questions/5262/rsa-and-prime-difference
    safedist = pow(2, exp)

    while abs(p - q) < safedist:
        q = generate_prime()

    phi = (p - 1) * (q - 1)

    # If this happens, then something went wrong.
    while not gcd(e, phi) == 1:
        p = generate_prime()
        q = generate_prime()
        while abs(p - q) < safedist:
            q = generate_prime()
        phi = (p - 1) * (q - 1)

    d = ext_eucl_alg(e, phi)

    # We need to calculate d (using Extended Euclidean Algorithm)
    return p * q, p, q, e, d


if __name__ == "__main__":
    genRSAkey(int(sys.argv[1]))
