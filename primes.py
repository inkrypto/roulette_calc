#!/usr/bin/python3

def isprime(n):
	if n <= 1:
		return False
	for x in range(2, n):
		if n % x == 0:
			return False
	else:
		return True

def list_primes():
	for n in range(100):
		if isprime(n):
			print(n , end=' ', flush=True)
	print

n = 6
if isprime(n):
	print('{} is prime'.format(n))
else:
	print('{} not prime'.format(n))

list_primes()
