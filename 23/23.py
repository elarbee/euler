#find every number that is a sum of two abundant numbers under 28123


#Returns the sum of the proper divisors of n
def d(n):
	l = range(1,(n/2)+1)
	l = filter(lambda x: n%x==0,l)
	return sum(l)

#def perfect(n):
#	return d(n) == n
#
#def deficient(n):
#	return d(n)<n

def abundant(n):
	return d(n)>n

#return a distinct list with all of the possible sums from a list
def all_possible_sums(l):
	sums = []
	for a in l:
		for b in l:
			sums.append(a+b)
	sums = set(sums)
	sums = list(sums)
	return sums

#All numbers above this can be created by summing abundant numbers
limit = 28123
abundant_nums = range(12,(limit/2)+1)
abundant_nums = filter(abundant,abundant_nums)

print "Abundant numbers list generated"

abundant_sums = all_possible_sums(abundant_nums)

# Remove Duplicates
abundant_sums = list(set(abundant_sums))

def summable(n):
	return n not in abundant_sums

# List of numbers that can not be created by summing abundant numbers
non_summable_nums = range(0,limit+1)
non_summable_nums = filter(summable, non_summable_nums)

print non_summable_nums[0:20]
print sum(non_summable_nums)

