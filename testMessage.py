#!/usr/bin/python3

import platform

def message():
	print("This version of python is {}".format(platform.python_version()))

def main():
	message()


if __name__ == '__main__': main()
