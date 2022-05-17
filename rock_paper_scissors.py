print("ROCK, PAPER, SCISSORS!") 

replay = "y" 

while replay == "y": #keeps going until user says they don't want to play or responds in a way other than y. 

	# how many players
	intro_q = input("How many players? Enter \"1\" or \"2\": ")
	intro_q = int(intro_q)

	#how many rounds
	out_of = input("How many rounds would you like to play? Enter a number. " )
	out_of = int(out_of)

	#setting/resetting wins to 0
	first_player_wins = 0
	second_player_wins = 0
	ties = 0

	for n in range(out_of): #repeats game the number of times the user requested above
		
		#Sequence for player input
		user1 = input("First Player: rock, paper, or scissors? ").lower() #user1 input for both 1 and 2 player versions.

		if intro_q == 2: #code to hide first player's input and allow second player to type in choice

			print("NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING")

			user2 = input("Second Player: rock, paper, or scissors? ").lower()

		elif intro_q == 1: #code for generated input from a computer
			import random
			computer = random.randint(1, 3)
			if computer == 1:
				user2 = "rock"
				print(f"Computer: {user2}")
			elif computer == 2:
				user2 = "paper"
				print(f"Computer: {user2}")
			else:
				user2 = "scissors"
				print(f"Computer: {user2}")
		else: #for if the user entered an invalid introq - exits program.
			print("Sorry, you did not type \"1\" or \"2\". Please restart and try again.")
			break

		#Sequence to determine who wins round
		if (user1 == "rock" and user2 == "scissors") or (user1 == "paper" and user2 == "rock") or (user1 == "scissors" and user2 == "paper"):
			print("First Player Wins!")
			first_player_wins += 1 # adding to win counter
		elif(user2 == "rock" and user1 == "scissors") or (user2 == "paper" and user1 == "rock") or (user2 == "scissors" and user1 == "paper"):
			if intro_q == 1:
				print("Computer Wins!")
			else:
				print("Second Player Wins!")
			second_player_wins += 1 # adding to win counter
		elif user1 == user2:
			print("It's a tie!")
			ties += 1 # adding to tie counter
		else:
			print("Something went wrong. Typo?") #nothing added to win or tie counters

	#sequence to determines who wins game
	if first_player_wins > (out_of/2):
		print (f"First player won {first_player_wins} rounds and wins the game!")
	elif second_player_wins > (out_of/2):
		if intro_q == 2: #for two player game
			print (f"Second player won {second_player_wins} rounds and wins the game!")
		if intro_q == 1: #for one player game
			print(f"Computer won {second_player_wins} rounds and wins the game!")
	else:
		print(f"It's a draw!")

	replay = input("Well done! Would you like to play again? (y/n) ").lower() #ends game if anything but "y" or "Y" are entered.

print("Thank you for playing! Goodbye!")
