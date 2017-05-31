import time
import itertools

start = time.time()

#Returns the sum of the proper divisors of n
def d(n):
	l = range(1,(n/2)+1)
	l = filter(lambda x: n%x==0,l)
	return sum(l)
	
def amicable(a,b):
	return d(a)==b and d(b)==a and a!=b

# Return sum of all amicable numbers under 10000
def solve():
	amicable_pairs = []
	number_set = range(0,10000)
	# a and b can only be even or divisible by 5 (this is cheating)
	#number_set = filter(lambda x: x%2==0 or x%5==0,number_set)
	
	for a in number_set:
		b = d(a)
		if amicable(a,b):
			amicable_pairs.append( (min(a,b), max(a,b)) )
	#Remove Dupes
	amicable_pairs = list(set(amicable_pairs))
	#Sum the tuples
	amicable_pairs = map(sum,amicable_pairs)
	#Sum the sums
	return sum(amicable_pairs)
print solve()


end = time.time()
print "Elapsed time: " + str(end - start)

