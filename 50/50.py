from EulerUtils.Tools import isPrime

sequence = range(0,1000)
primes = filter(isPrime, sequence)

# slice_list(l,n)
# abcdefg
# abcdef bcdefg
# abcde bcdef cdefg
# acbd bcde cdef defg
# abc bcd cde def efg
# ab bc cd de ef fg
# a b c d e f g h i

def slice_list(l,n):
    slices = []
    for i in range(0,len(l)):
        if i+n<len(l):
            slices.append(l[i:i+n])
    return slices

def solve():
    for i in reversed( range(1,len(primes)) ):
        for slice in slice_list(primes,i):
            s = sum(slice)
            if isPrime(s) and s<1000:
                return s

print solve()
