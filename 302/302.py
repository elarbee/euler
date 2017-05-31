from EulerUtils.Tools import Factors, PrimeFactors, isPrime
import math
from fractions import gcd


def Powerful(n):
    p = PrimeFactors(n)
    # If there are no prime factors, False.
    if len(p) == 0:
        return False
    p2 = map(lambda x:x**2,p)
    for i in p2:
        if n % i != 0 or n ==0:
            return False
    return True


# https://en.wikipedia.org/wiki/Perfect_power#Detecting_perfect_powers
def Perfect(n):
    if n <= 0:
        return False
    end = math.log(n,2)+1
    k = range(1,int(math.ceil(end)))
    k = filter(isPrime,k)

    f = Factors(n)
    values = []
    for i in f:
        values+= map(lambda x:i**x,k)
    values = set(values)
    return n in values


def not_perfect(n):
    return not Perfect(n)


def Achilles(n):
    return Powerful(n) and not_perfect(n)


def phi(n):
    r = range(1,n)
    r = filter(lambda x:gcd(x,n)==1,r)
    return len(r)


def Strong_Achilles(n):
    return Achilles(n) and Achilles(phi(n))

r = range(2, (10**4)+1)
r = filter(Strong_Achilles, r)

print r
print len(r)
