# ideas:

import random  # import module random

myNumber = random.randint(0, 100)  # define a random number to guess
difficulty = str(input("Choose difficulty:\n\tHard\n\tMedium\n\tEasy\n"))  # define difficulty and mistake's count
if difficulty == "Hard":
    difficulty = 3
elif difficulty == "Medium":
    difficulty = 2
elif difficulty == "Easy":
    difficulty = 1
mistakeCount = 0
if difficulty == 3:
    mistakeCount = 3
elif difficulty == 2:
    mistakeCount = 6
elif difficulty == 1:
    mistakeCount = 10
n = 0  # variable to define previous difficulty, if user will not change a difficulty
userChoice = int(input("Try to guess my number:\n"))  # define a user attempt
playAgain = 1
while (playAgain == 1) and (mistakeCount > 0):  # cycle to help user
    if userChoice < myNumber:
        print("My number is more, try again")  # try to help user and overwrite variable to continue cycle
        userChoice = (int(input()))
        mistakeCount -= 1  # reduce this variable to count of mistakes
        n += 1
    elif userChoice > myNumber:  # -//-
        print("My number is less, try again")
        userChoice = (int(input()))
        mistakeCount -= 1
        n += 1
    elif userChoice == myNumber:
        print("You guess! Congratulation!")
        print("Do u wanna play one more? Yes/No?")  # ask user, would he like to play again?
        userWish = input()  # check his answer
        if userWish == "Yes":  # if he answer is "yes", rewrite three variables to continue cycle WHILE
            print("Do u wanna change a difficulty? Yes/No?")  # aks user whether he wants to change difficulty?
            changeDifficulty = input()
            if changeDifficulty == "Yes":
                difficulty = str(input("Choose difficulty:\n\tHard\n\tMedium\n\tEasy\n"))
                if difficulty == "Hard":
                    difficulty = 3
                elif difficulty == "Medium":
                    difficulty = 2
                elif difficulty == "Easy":
                    difficulty = 1
                mistakeCount = 0
                if difficulty == 3:
                    mistakeCount = 3
                elif difficulty == 2:
                    mistakeCount = 6
                elif difficulty == 1:
                    mistakeCount = 10
                n = 0  # null the variable to change difficulty
                playAgain = 1
                myNumber = random.randint(0, 100)
                userChoice = int(input())
            else:
                playAgain = 1
                myNumber = random.randint(0, 100)
                userChoice = int(input())
                mistakeCount = n  # equalize this variables to difficulty has not changed

        else:
            playAgain = 0  # else: cycle ends
if mistakeCount == 0:  # if user loses, print accordingly message
    print("Unfortunately, you lose!")
else:
    print("Thanks for the playing!")
