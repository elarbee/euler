# Functions used repeatedly in project Euler

def isPrime(n):
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

# Normal Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Takes int, returns a list of the ints digits
def digits(n):
    n = str(n)
    n = list(n)
    n = map(int,n)
    return n

# Returns List of factors
def Factors(n):
    r = range(1, (n/2)+1)
    r = filter(lambda x:n%x==0,r)
    return r

def PrimeFactors(n):
    f = Factors(n)
    return filter(isPrime, f)
