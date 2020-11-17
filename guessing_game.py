#  Python Web Development Techdegree
#  Project 1 - Number Guessing Game
#  --------------------------------

import random

play_again = "Y"
high_score = 4

def start_game():
    print("\n***********************\nWelcome to Number Guessers {}, the most exhilirating game ever invented!\n".format(name))
    print("A number has been chosen between 1 and 10. Bet ya can't guess what it is.")
    print("The current high score is {} guesses.".format(high_score))
    
print("\n### NUMBER GUESSERS ####\n")
name=input("Hello, what's your name?   ")

while play_again != "N":
    start_game()
    guess = 0
    number_of_guesses = 0
    correct_number = random.randint(1,10)

    while guess != correct_number:
        try:
            guess = int(input("\nWhat number do you guess?    "))
            if guess >10 or guess <1:
                raise ValueError
        except ValueError:
            print("Oops, you must enter a number between 1 and 10. Let's try that again.")
        else:
            number_of_guesses += 1 
            if guess < correct_number:
                print("It's higher, try again")
            elif guess > correct_number:
                print("It's lower, try again")
            else:
                print("\nGot it!\nThat took you {} attempt/s\n".format(number_of_guesses))
                if number_of_guesses < high_score:
                    print("Congrats {}, that's the new high score!\n".format(name))
                    high_score = number_of_guesses
                play_again = input("Would you like to play again? Y/N   ").upper()
                while play_again != "Y" and play_again != "N":
                    play_again = input("\nOops! You must put in a Y or N.\nWould you like to play again? Y/N   ").upper()


print("\nThe game is over, have a great day!") 

