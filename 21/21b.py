#https://www.daniweb.com/programming/software-development/code/216880/check-if-a-number-is-a-prime-number-python
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
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

#If this returns 3 prime numbers than we can generate an amicable pair with n
def amicable_seed_check(n):
	p1 = 3 * (2**n) - 1
	p2 = 3 * (2**(n+1)) - 1
	p3 = (3**2) * (2**((2*n)+1)) - 1
	return isPrime(p1) and isPrime(p2) and isPrime(p3)

def amicable_pair(n):
	a = (2**(n+1))*(3 * (2**n) - 1)*(3 * (2**(n+1)) - 1)
	b = (2**(n+1)) * ( (3**2) * ((2**((2*n)+1)))-1) 
	return (a,b)
i=1
while True:
	if amicable_seed_check(i):
		print amicable_pair(i)
	i+=1