one_p = 0.01
two_p = 0.02
five_p = 0.05
ten_p = 0.1
twenty_p = 0.2
fifty_p = 0.5
one_pound = 1
two_pound = 2

coins = [one_p, two_p, five_p, ten_p, twenty_p, fifty_p, one_pound, two_pound]

def make_change(n)
	purse = []
	total=0
	for coin in reversed(coins):
		total+=coin
		if total=n:

