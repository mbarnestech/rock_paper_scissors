print("ROCK, PAPER, SCISSORS!") 

replay = "y" 

while replay == "y": #keeps going until user says they don't want to play or responds in a way other than y. 

	# how many players
	intro_q = input("How many players? Enter \"1\" or \"2\": ")
	intro_q = int(intro_q)

	#how many rounds
	out_of = input("How many rounds would you like to play? Enter a number: " )
	out_of = int(out_of)

	#setting/resetting wins to 0
	first_player_wins = 0
	second_player_wins = 0
	ties = 0

	for n in range(out_of): #repeats game the number of times the user requested above
		
		#Sequence for player input
		user1 = input("First Player: rock, paper, or scissors? ").lower()[0] #user1 input for both 1 and 2 player versions.

		if user1 == "q":
			break

		elif intro_q == 2: #code to hide first player's input and allow second player to type in choice

			print("NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING")

			user2 = input("Second Player: rock, paper, or scissors? ").lower()[0]

		elif intro_q == 1: #code for generated input from a computer
			import random
			computer = random.randint(1, 3)
			if computer == 1:
				user2 = "rock"
			elif computer == 2:
				user2 = "paper"
			else:
				user2 = "scissors"
			print(f"Computer: {user2}")
			user2 = user2[0]

		else: #for if the user entered an invalid introq - exits program.
			print("Sorry, you did not type \"1\" or \"2\". Please restart and try again.")
			break

		#Sequence to determine who wins round
		if (user1 == "r" and user2 == "s") or (user1 == "p" and user2 == "r") or (user1 == "s" and user2 == "p"):
			print("First Player Wins!")
			first_player_wins += 1 # adding to win counter
		elif(user2 == "r" and user1 == "s") or (user2 == "p" and user1 == "r") or (user2 == "s" and user1 == "p"):
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
	if first_player_wins > second_player_wins:
		print (f"First player won {first_player_wins} rounds and wins the game!")
	elif second_player_wins > first_player_wins:
		if intro_q == 2: #for two player game
			print (f"Second player won {second_player_wins} rounds and wins the game!")
		if intro_q == 1: #for one player game
			print(f"Computer won {second_player_wins} rounds and wins the game!")
	else:
		print("Nobody wins - the game is a draw!")

	if user1 == "q":
		replay = "n"
	else:
		replay = input("Would you like to play again? (y/n) ").lower()[0] #ends game if anything but "y" or "Y" are entered.
	#replay = replay[0]

print("Thank you for playing! Goodbye!")
