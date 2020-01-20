import random
import time

while True:
	player_move = input("Enter your move please. (Rock/Paper/Scissors) )
	while (((((player_move != "Rock") and player_move != "Scissors") and player_move != "Paper") and player_move != "Nuke") and player_move != "ICBM"):
		time.sleep(3)
		print ("Input failed. Please type again")
		player_move = input("Enter your move please. (Rock/Paper/Scissors) ")
	computer_move = random.random()
	if computer_move <= 0.33:
		computer_move = "Rock"
	elif computer_move <= 0.66:
		computer_move = "Paper"
	else:
		computer_move = "Scissors"
		
	print(" ")
	time.sleep(1))
	print("Rock")
	time.sleep(1)
	print("Paper")
	time.sleep(1)
	print("Scissors")
	time.sleep(1)
	print("Shoot!")
	print("  ")
	time.sleep(1)
	
	if computer_move == player_move:
		print("It is a tie")
	elif ((computer_move == "Rock") and (player_move == "Scissors")) or\
	((computer_move == "Scissors") and (player_move == "Paper")) or\
	((computer_move == "Paper") and (player_move == "Rock")):
		print("Computer move: " + computer_move + ". You lose")
	else:
		print("Computer move: " + computer_move + ". You won!")
		
	CloseMech = input("Do you want to try again? (Yes/No) ")
	while ((CloseMech != "Yes") and CloseMech != "No"):
		time.sleep(3)
		print ("Input failed. Please type again.")
		CloseMech = input(" Do you want to try again? (Yes/No) ")
	
	if ((CloseMech == "No")):
		break
	elif (CloseMech == "Potato"):
		print ("Spaace potaaattoooo")