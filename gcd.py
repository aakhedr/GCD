def naive_gcd(a, b):
	"""
	a, b = Integers
	Find greatest common divisor the easy naive way.	
	"""
	best = 0
	for d in range(1, min([a, b])):
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

import time
import random

def stressTest():
	"""
	Output of both functions should be identical.
	Runtime should be faster with 'eucledian_gcd'.
	"""
	lower_bound = 0
	upper_bound = 1000000

	as_and_bs = []			# A list of a and b (tuples)
	n = 10 					# Number of tests
	for i in range(n):
		a = random.randrange(lower_bound, upper_bound)
		b = random.randrange(lower_bound, upper_bound)
		as_and_bs.append((a, b))
	
	for t in range(len(as_and_bs)):
		t1 = time.time()
		slow_gcd = naive_gcd(as_and_bs[t][0], as_and_bs[t][1])
		t2 = time.time()
		diff1 = t2 - t1

		t3 = time.time()
		fast_gcd = eucledian_gcd(as_and_bs[t][0], as_and_bs[t][1])
		t4 = time.time()
		diff2 = t4 - t3

		if slow_gcd == fast_gcd:
			print("GCD of:", str(as_and_bs[t]), "is equal by both functions:", fast_gcd)
		else:
			print("GCD of:", str(as_and_bs[t]), "is NOT equal by both functions.", "'slow_gcd'=", slow_gcd, "'fast_gcd'=", fast_gcd)
		
		if diff1 > diff2:
			print("'eucledian_gcd' faster than 'naive_gcd'")
		elif diff1 < diff2:
			print("'naive_gcd' faster than 'eucledian_gcd'")
		else:
			print("both functions were computed in equal times")
		
		if t != (len(as_and_bs) - 1):
			print("")
