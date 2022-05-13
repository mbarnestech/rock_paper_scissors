print("ROCK, PAPER, SCISSORS!")
intro_q = input("How many players? Enter \"1\" or \"2\" ")


user1 = input("First Player: rock, paper, or scissors? ")

if int(intro_q) == 2:

	print("NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING")

	user2 = input("Second Player: rock, paper, or scissors? ")

elif int(intro_q) == 1:
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
else: 
	print("Sorry, please try again")

if (user1 == "rock" and user2 == "scissors") or (user1 == "paper" and user2 == "rock") or (user1 == "scissors" and user2 == "paper"):
	print("First Player Wins!")
elif(user2 == "rock" and user1 == "scissors") or (user2 == "paper" and user1 == "rock") or (user2 == "scissors" and user1 == "paper"):
	print("Second Player Wins!")
elif user1 == user2:
	print("It's a tie!")
else:
	print("Something went wrong. Typo?")
