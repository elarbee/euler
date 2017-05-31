s = range(1,1001)
s_prime = map(lambda x:x**x,s)
print str(sum(s_prime))[-10:]