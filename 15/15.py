# Euler problem 15
# Number of grid paths is equal to a binomial coefficient


# Inefficient Recursive formula
# https://en.wikipedia.org/wiki/Binomial_coefficient#Recursive_formula
def recursive_binomial_coefficient(n, k):
    if k == n:
        return 1
    if k == 0 and n >= 0:
        return 1
    bc_1 = recursive_binomial_coefficient(n - 1, k - 1)
    bc_2 = recursive_binomial_coefficient(n - 1, k)
    return bc_1 + bc_2


# Takes the product of every item in a list i.e. a * b * c
def list_product(l):
    return reduce(lambda y, z: y * z, l, 1)


# Falling factorial
def falling_factorial(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    ff = range(1, n)
    ff = map(lambda y: x - y, ff)
    ff = x * list_product(ff)
    return ff


# Normal Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# More efficient multiplicative method
def multiplicative_binomial_coefficient(n, k):
    return falling_factorial(n, k) / factorial(k)


print multiplicative_binomial_coefficient(40, 20)
