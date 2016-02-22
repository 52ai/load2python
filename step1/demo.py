'''
	Create on 2016-02-22
	@author:Wenyan Yu
'''

def factorial(n):
	if n==1:
			return 1
	else:
		return n*factorial(n-1)

print factorial(10)
	