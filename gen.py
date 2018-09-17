#!/usr/bin/python3

def main():
	for i in inclusive_range(5, 200, 5):
		print(i, end = ' ')
	print()

def inclusive_range(*args):
	numargs = len(args)
	start = 0
	step = 1
	
	#init params
	if numargs < 1:
		raise TypeError('excpecting at least 1 arg, got {}'.format(numargs))
	elif numargs == 1:
		stop = args[0]
	elif numargs == 2:
		(start, stop) = args
	elif numargs == 3:
		(start, stop, step) = args
	else:
		raise TypeError('excpecting at most 3 args, got {}'.format(numargs))
		
	#generator
	i = start
	while i <= stop:
		yield i
		i += step

if __name__ == '__main__': main()

