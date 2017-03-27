"""
Exercise 8 (and Solution)

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

"""

def winner(choices):
    """Compare options against rules and return the winning player's index in choices list after adding 1"""
    if choices[0] == 'rock':
        if choices[1] == 'scissors':
            return 1
        return 2
    if choices[0] == 'scissors':
        if choices[1] == 'paper':
            return 1
        return 2
    if choices[0] == 'paper':
        if choices[1] == 'rock':
            return 1
        return 2

choices = []
player = 1

while True:
    while True:

        choice = input("Player {0}: Rock? Scissors?? Paper??? Enter your choice: ".format(player))
        choice = choice.lower()
        if not choice:
            print("You have not entered your choice. Try again!!!")
            continue
        if choice not in ['rock', 'scissors', 'paper']:
            print("You entered an invalid choice. Try again!!!")
            continue
        if player == 2 and choice in choices:
            print("You both entered same choice. Try again!!!")
            continue
        choices.append(choice)
        player += 1
        if len(choices) == 2:
            break

    print ("Player {0} WON!!! Congratulations!!!".format(winner(choices)))
    choices = []
    player = 1
    if (input ("Do you want to play again? (y/n): ").lower() != "y"):
        break
