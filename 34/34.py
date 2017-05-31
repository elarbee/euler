from EulerUtils.Tools import factorial, digits

def sum_of_factorial(n):
    n = digits(n)
    n = map(factorial,n)
    return sum(n)

i = 3
s = 0
while True:
    if i == sum_of_factorial(i):
        s += i
        print s
    i+=1