#!/usr/bin/python3

secret = "blowfish"
pw =  " "
auth = False
count = 0
max_attempt = 5

while pw != secret:
	count += 1
	pw = input("{} What is the correct password! ".format(count))
	if count == max_attempt:
		break
else:
	auth = True
	
	#if pw == secret:
	#	print("Welcome to hell!")

print("Authorized" if auth else "Fuck off!!!") 
