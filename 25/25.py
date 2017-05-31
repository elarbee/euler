fibbonacci_sequence = [0,1]

for i in range(0,10000):
	length = 2
	n = fibbonacci_sequence[i]
	m = fibbonacci_sequence[i+1]
	o = n+m
	digit_len = len(str(o))
	fibbonacci_sequence.append(n+m)
	if digit_len==1000:
		print i+2
		break



