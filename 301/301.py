def nim(a,b,c):
    return a^b^c

limit = 2**30

num_zeroes = 0

i = 1

while i < limit + 1:
    if nim(i, 2*i, 3*i) == 0:
        num_zeroes += 1
    print (i+0.0)/limit
    i += 1

print num_zeroes