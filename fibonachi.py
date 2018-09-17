#!/usr/bin/env python3

#fibonacci sequence = the sum of 2 elements defines the next set

a, b = 0, 1
while b < 1000:
	print(b, end = '', flush = True)
	a, b = b, a + b

print() #line ending
