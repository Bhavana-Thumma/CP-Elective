# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isprime(x):
	if(x<2 or (x%2 == 0 and x!= 2)):
		return False
	for i in range(3, x//2, 2):
		if(x%i == 0):
			return False
	return True
	
def powerfulnumber(x):
	if(x == 1):
		return True
	if(isprime(x)):
		return False      
	for i in range(2,x//2+1):
		if(x%i==0 and isprime(i) and x%(i*i)!=0):
			return False
	return True
			
def nthpowerfulnumber(n):
	f = 0
	g = 0
	while(f<=n):
		g+=1
		if(powerfulnumber(g)):
			f+=1
	return g