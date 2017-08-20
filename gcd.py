def naive_gcd(a, b):
	"""
	
	"""
	best = 0
	for d in range(1, max([a, b])):
		if (a % d == 0) and (b % d == 0):
			best = d
	return best

def eucledian_gcd(a, b):
	"""

	"""
	if b == 0:
		return a
	a_prime = a % b
	return eucledian_gcd(b, a_prime)

