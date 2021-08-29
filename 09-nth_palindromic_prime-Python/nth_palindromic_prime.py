# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2

def isprime(x):
	if(x<2 or (x%2 == 0 and x!= 2)):
		return False
	for i in range(3, x//2, 2):
		if(x%i == 0):
			return False
	return True
def fun_nth_palindromic_prime(n):
	f = 0
	g = 0
	while(f<=n):
		g+=1
		if(isprime(g) and str(g)==str(g)[::-1]):
			f+=1
	return g