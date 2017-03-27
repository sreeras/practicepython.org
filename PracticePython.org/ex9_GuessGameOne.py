"""
Exercise 9 (and Solution)

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

from random import randint

while True:
    number = randint(1,9)
    print ("Need to guess", number)
    guessChance = 1
    while True:
        while True:
            try:
                guess = int(input("Guess# {0}: Enter a number between 1 and 9.".format(guessChance)))
                if guess not in range(1, 10):
                    print("Number wasn't between 1 and 9. Try again!!!\n\n")
                    continue
                break
            except:
                print ("That wasn't a number. Try again!!!\n\n")

        if(guess == number):
            print("Yes, that's {0}. You guessed the number in {1} chance(s).".format(number, guessChance))
            break
        elif (guess > 6) and (number < 4):
            print("Guess was too high!!!")
        elif (number > 6) and (guess < 4):
            print("Guess was too low!!!")
        guessChance += 1

    if(input("Do you want to continue? (y/n)").lower() != 'y'):
        break
