from random import randint

rep = "y"

while rep == "y": #anything that doesn't reduce to y in future input will stop the loop
	guess = input("Choose a number between 1 and 10: ").lower()
	if guess == "q" or guess =="quit": #giving users an out
			break
	else:
		guess = int(guess)
	num = randint(1, 10)
	while guess != num:
		if num > guess and num < 11:
			guess = input("Too low! Guess again: ")
		elif num < guess and num > 0:
			guess = input("Too high! Guess again: ")
		else:
			guess = input("That's not a number between 1 and 10! Try again: ")
		
		if guess == "q" or guess =="quit": #quits out of this while loop
			break
		else:
			guess = int(guess)

	if guess == "q" or guess =="quit": #
		print("Thank you for playing!")
		rep = "n"
	else:
		rep = input("Well done! Would you like to play again? Enter \"y\" or \"n\": ").lower()[0] #user can use any case letters and type in variants of yes and no starting with y and n. 