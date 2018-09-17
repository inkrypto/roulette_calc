#!/usr/bin/python3
#wrapper example

import time

def elapsed_time(f):						#this sets up the function(f)
	def wrapper():
		t1 = time.time()
		f()									#this is a function but you don't need a :
		t2 = time.time()
		print('Elapsed time: {} ms'.format(t2-t1))
		print()
	return wrapper

@elapsed_time								#like doing x = elapsed_time()
def big_sum():
	num_list = []
	for num in range(0, 10000):
		num_list.append(num)
	print('Big sum: {}'.format(sum(num_list)))
	print()

def main():
	big_sum()								#like doing this, big_sum(x())

if __name__ == '__main__': main() 
