from random import randint

rep = "y"

while rep != "n":
	guess = input("Choose a number between 1 and 10: ")
	guess = int(guess)
	num = randint(1, 10)
	while guess != num:
		if num > guess and num < 11:
			guess = input("Too low! Guess again: ")
		elif num < guess and num > 0:
			guess = input("Too high! Guess again: ")
		else:
			guess = input("That's not a number between 1 and 10! Try again: ")
		guess = int(guess)
	rep = input("Well done! Would you like to play again? Enter \"y\" or \"n\": ")