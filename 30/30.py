
def sum_of_nth_power(s,n):
    # 1 not allowed
    if s == 1:
        return False
    # Store in temp variable
    temp = s
    # Convert to string
    temp = str(temp)
    # Convert to char array
    temp = list(temp)
    # Convert to int array
    temp = map(int, temp)
    # Perform x**n on int array
    temp = map(lambda x: x**n, temp)
    # Calculate sum of int array
    temp = sum(temp)

    return s == temp

s = 0
i = 2
while True:
    if sum_of_nth_power(i,5):
        s+=i
        print s
    i+=1