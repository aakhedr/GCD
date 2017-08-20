def naive_gcd(a, b):
	"""
	
	"""
	best = 0
	for d in range(1, max([a, b])):
		if (a % d == 0) and (b % d == 0):
			best = d
	return best

