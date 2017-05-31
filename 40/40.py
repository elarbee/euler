

def d(n):
    champernowne_constant = ""
    champernowne_digits = len(champernowne_constant)
    i = 1
    while champernowne_digits<n:
        champernowne_constant+=str(i)
        i+=1
        champernowne_digits = len(champernowne_constant)
    return int(champernowne_constant[n-1])

print d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
