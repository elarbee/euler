import string

alphabet = list(string.ascii_uppercase)

names = file("./names.txt")
names = names.read().replace('"','').split(",")
names = sorted(names,key=str.lower)

def name_score(name):
	name = name.upper()
	name = list(name)
	score = map(lambda x:alphabet.index(x)+1,name)
	return sum(score)

names = map(name_score,names)
names = enumerate(names)
names = list(names)
names = map(lambda (x,y):(x+1)*y,names)
print sum(names)
