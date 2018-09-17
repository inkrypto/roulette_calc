#!/usr/bin/python3

def main():
	a = set("we're going to need a bigger boat.")
	b = set("I'm sorry dave. I can't do that.")
	#print_set(sorted(a))
	print_set(a ^ b)  			#in a but not b

def print_set(o):
	print('{', end='')
	for x in o: print(x, end='')
	print('}')

if __name__ == '__main__': main()

