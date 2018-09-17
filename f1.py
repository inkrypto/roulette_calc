#!/usr/bin/python3

def f1(f):
	def f2():
		print('this is before function call')
		f()
		print('this is after function call')
	return f2

@f1
def f3():
	print('this is f3')

print(f3())
