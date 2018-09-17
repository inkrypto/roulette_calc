#!/usr/bin/python3

def main():
	x = dict(Buffy='cat', zilla = 'jat', angel = 'git')
	kitten(**x)

def kitten(**kwargs):
	if len(kwargs):
		for s in kwargs:
			print('kitten {} says {}'.format(s, kwargs[s]))
	else:
		print('meow')
	
if __name__ == '__main__': main()
