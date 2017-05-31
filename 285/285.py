import random
import math
def albert(k):
    #a, b = random.random()
    a = 0.2
    b = 0.85
    component_a = ((k * a) + 1) ** 2
    component_b = ((k * b) + 1) ** 2

    square_root_of_sum = math.sqrt(component_a + component_b)

    rounded_square = round(square_root_of_sum)

    diff = rounded_square - k

    if abs(diff)<0.001:
        return k
    else:
        return 0

print sum( map(albert,range(1,11)))