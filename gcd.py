def naive_gcd(a, b):
	"""
	a, b = Integers
	Find greatest common divisor the easy naive way.	
	"""
	best = 0
	for d in range(1, max([a, b])):
		if (a % d == 0) and (b % d == 0):
			best = d
	return best

def eucledian_gcd(a, b):
	"""
	a, b = Integers
	Use Eucledian method to find GCD where GCD(a, b) = GCD(b, a`) 
	"""
	if b == 0:
		return a
	a_prime = a % b
	return eucledian_gcd(b, a_prime)

