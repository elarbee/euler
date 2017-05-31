from collections import deque


def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
        # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def is_circular_prime(n):
    if not isprime(n):
        return False
    n = str(n)
    d = deque(n)
    for i in range(0,len(n)-1):
        d.rotate(-1)
        temp = "".join(list(d))
        temp = int(temp)
        if not isprime(temp):
            return False
    return True



r = range(2,1000000)
r = filter(is_circular_prime,r)
print len(r)
