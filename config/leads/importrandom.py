import random
def randcountry(fname):
	lines=open(fname).read().splitlines()
	config = random.choice(lines)
	return config

