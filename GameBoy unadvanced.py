""""Select a game!
1. Roulette
2. Math Quiz
3. The Waiting Game
4. Quit
After this it should take an input for the number corresponding to the game. Be sure to error check that the number is indeed between 1 and 4.
If not, please output Invalid selection. Please pick a valid game number. and ask again.
The Selections should use functions to run the particular game. If you code the entire game within the if condition, it'll be points off.
roulette:
At the beginning seed the random number generator with the seed 10 with random.seed(10) This is for grading purposes.
Afterwards, generate a random number between 1 and 10. Prompt the player to guess by asking 
Guess a number between 1 and 10: 
If the guess right, print You Win! Otherwise print Wrong! Guess again! before prompting them for another input with the same message as above.
mathQuiz:
As before, seed the random number generator with the seed 10. Now generate 2 random numbers and ask the user
What is {firstNumber} + {secondNumber}? 
If they guess right, once again print You Win! and if they guess wrong print Wrong! Guess again! before repeating the same prompt as above. 
theWaitingGame:
Wait 5 seconds, then print You Win! then return.
Upon completion of any game, the game selection should repeat to prompt the user to select another game. This should only end if the user inputs 4 as their game selection in order to quit.

import random
import time
import sys

#Roulette
def roulette():
    print("Guess a Number between 1 and 10!")
    random.seed(10)
    number = random.randint(1, 10)
    while True:
        guess = int(input(''))
        if guess == number:
            print("You Win!")
            Select_Page()
            break
        else:
         print("Wrong! Guess Again!")

def mathQuiz():
    random.seed(10)
    Num_1 = random.randint(1,10)
    Num_2 = random.randint(1,10)
    Solution = Num_1 + Num_2
    print(f"What is {Num_1} + {Num_2}")
    while True: 
        Try = int(input(''))
        if Try == Solution:
            print("You Win!")
            Select_Page()
            break
        else:
            print("Wrong! Guess Again!")

def WaitingGame():
    time.sleep(5)
    print("You Win!")
    Select_Page()

def Exit_Program():
    sys.exit(0)

#Game select Page
def Select_Page():
    print("Select a game!\n 1. Roulette\n 2. Math Quiz\n 3. The Waiting Game\n 4. Quit")
    num = int(input(''))
    while (num < 1 or num > 4):
            print("Invalid Selection. Please pick a valid game number.")
    if num == 1:
        roulette()    
    elif num == 2:
        mathQuiz()
    elif num == 3:
        WaitingGame()
    else:
        Exit_Program()
        
Select_Page()"""

    

