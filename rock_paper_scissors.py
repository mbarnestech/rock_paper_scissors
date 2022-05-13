user1 = input("First Player: rock, paper, or scissors? ")

print("NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING \n \n NO CHEATING")

user2 = input("Second Player: rock, paper, or scissors? ")

if (user1 == "rock" and user2 == "scissors") or (user1 == "paper" and user2 == "rock") or (user1 == "scissors" and user2 == "paper"):
	print("First Player Wins!")
elif(user2 == "rock" and user1 == "scissors") or (user2 == "paper" and user1 == "rock") or (user2 == "scissors" and user1 == "paper"):
	print("Second Player Wins!")
else:
	print("It's a tie!")