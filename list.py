#!/usr/bin/python3

def print_list(o):
	for x in o: print(x, end='')  	#two things on same line
	print()

def main():
	seq = range(11)
	#seq2 = [x for x in seq if x % 3 == 0] 	#set the variable do for loop then if statement
	#from math import pi
	#seq2 = [round(pi, i) for i in seq]  #rounding to pi
	#seq2 = [(x, x**2) for x in seq] 	#list of tuples
	#seq3 = {x: x**2 for x in seq} 
	print_list(seq)
	#print_list(seq2)
	#print(seq3) 		#can't use pring_list but can use print to print dict
	seq4 = {x for x in 'superdupa' if not x in 'pd'}
	print(seq4)

if __name__ == '__main__': main()
