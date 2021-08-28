# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isprime(x):
	if(x<2 or (x%2 == 0 and x!= 2)):
		return False
	for i in range(3, x//2, 2):
		if(x%i == 0):
			return False
	return True
def digitsum(x):
	s = 0
	while(x>0):
		s += x%10
		x//=10
	return s
def additiveprime(x):
	if(isprime(x) and isprime(digitsum(x))):
		return True
	return False
def fun_nth_additive_prime(n):
	f = 0
	g = 0
	while(f<=n):
		g+=1
		if(additiveprime(g)):
			f+=1
	return g