from EulerUtils.Tools import isPrime

sequence = range(1000,10000)
primes = filter(isPrime,sequence)

max_diff = primes[-1:][0] - primes[0]

#n
#a,(a+n),(a+2n) = prime,prime,prime

def is_prime_sequence(a,n):
    b = a+n
    c = a+(2*n)
    if not is_permutation(a,b) or not is_permutation(a,c) or not is_permutation(b,c):
        return False
    if not isPrime(a):
        return False
    if not isPrime(a+n):
        return False
    if not isPrime(a+(2*n)):
        return False
    return True

# is b a permutation of a
def is_permutation(a,b):
    return sort_digits(a) == sort_digits(b)


def sort_digits(n):
    n = str(n)
    n = list(n)
    n = sorted(n)
    return n


for n in primes:
    # The difference of every number in the prime sequence relative to n
    diffs = map(lambda x:x-n,primes)
    diffs = filter(lambda x:x>0,diffs)
    for d in diffs:
        if is_prime_sequence(n,d):
            if n!=1487:
                print str(n) + str(n+d) + str(n+(d*2))
                break

