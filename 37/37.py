from EulerUtils.Tools import isPrime, digits

def right_trucate(n):
    length = len(str(n))
    if isPrime(n) == False:
        return False
    elif length == 1:
        return True
    elif length>1:
        n = str(n)
        n = n[:-1]
        n = int(n)
        return right_trucate(n)

def left_trucate(n):
    length = len(str(n))
    if isPrime(n) == False:
        return False
    elif length == 1:
        return True
    elif length>1:
        n = str(n)
        n = n[1:]
        n = int(n)
        return left_trucate(n)
def truncatable(n):
    return left_trucate(n) and right_trucate(n) and n not in (2,3,5,7)

i = 1
trunc_primes = []
num_trunc_primes = 0
while num_trunc_primes < 11:
    if truncatable(i):
        trunc_primes.append(i)
        num_trunc_primes +=1
    i +=1

print sum(trunc_primes)


