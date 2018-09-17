#!/usr/bin/python3

def main():
	game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
	i = game.index('Spock')
	game.insert(0,'weed')
	del game[1:3]
	print(i)
	print_list(game)

def print_list(o):
	for i in o:
		print(i, end=' ', flush=True)

if __name__ == '__main__': main()
