def streak(n):
    k = 1
    while True:
        if (n+k)%k != 0:
            return k-1
        k+=1
        n+=1

def P(s,N):
    r = range(1,N)
    r = map(streak, r)
    r = filter(lambda x: x ==s, r)
    return len(r)

print P(3,14)