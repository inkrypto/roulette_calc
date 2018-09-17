#!/usr/bin/python3

import pdb

def main():

	animals = dict(cat = 'meow', dog = 'bark', snake = 'hiss', bird = 'cacawww', squirel = 'squeak')
	for k in animals.keys():print(k)
	print('found cat' if 'bat' in animals else 'cat dead')
	print(animals.get('snake'))

def print_dict(o):
	for k, v in o.items():
		print('{}: {}'.format(k, v))

if __name__ == '__main__': main()
