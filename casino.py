#!/usr/bin/python
# Roulette Calculator
# this is simple math program to calculate how much money you'd win if you put $$$ first on either red or black
# then put that entire amount on one number
# Why? because I am in Vegas ATM and this is more fun . . .

def bet():

	bet = input("How much do you want to bet on Red or Black? ")
	red_or_black = input("How many bets do you want to make? ")		#num tries on or red/black
	total = bet * (2 ** red_or_black)					#formula = x(2^y)
	odds = 37								#odds of winning 37 to 1
	total_winnings = total * odds

	print('A winning ${} bet on red or black {} times, would yield ${}'.format(bet, red_or_black, total))
	print("Taking those winnings then betting it all on one number, you'd win ${}!!!".format(total_winnings))
	print('Winner winner chicken dinner!')

def main():
	bet()

if __name__ == '__main__': main()
