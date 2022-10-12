import random

hand_signs = ["rock", "paper", "scissors"]
round = 1
user_wins = 0
computer_wins = 0

while True:

    print("********ROUND: ", round, "***********")
    user_choice = input("Pick: rock/paper/scissors or Q to quit: ").lower()
    round += 1

    r = random.randint(0, 2)
    computer_choice = hand_signs[r]

    

    if user_choice == "q":
        quit()

    elif user_choice not in hand_signs:
        print("\n------wrong input------\n")

    else:

        print("\nUser picked:", user_choice)
        print("Computer picked:", computer_choice, "\n")

        if user_choice == computer_choice:
            print("DRAW!")

        elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper":
            print("user wins")
            user_wins += 1

        else:
            print("computer wins")
            computer_wins += 1 

    print("*Score Board* \n user:{0}  computer:{1} \n".format(user_wins, computer_wins))       

    if user_wins == 3:
        print("Winner: User")
        quit()
    
    elif computer_wins == 3:
        print("Winner: Computer")
        quit()

        


    



