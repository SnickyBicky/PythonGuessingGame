import sys
from random import randint

def gameMenu() : 
    #Display welcome message and initial menu to user.
    
    print('\nHello, welcome to my Guess the Number Game!\n')
    print('Are you ready...?')
    menuChoice = input('Press Y to start game, or X to quit.\n\n').upper()

    menuLoop = True

    while menuLoop :

        clearConsole(0)

        if menuChoice == "Y" :
            clearConsole(0)
            playGame()

        elif menuChoice == "X" :
            clearConsole(0)
            sys.exit()

        else :
            gameMenu()

    
def playGame() :
    #Obtain input from user, check against random number and display output

    intLower = 0 #default set to 0
    intHigher = 100 #default set to 100
    rndNumber = 0
    
    print('\nThe number will be from an inclusive range of {0} to {1}'.format(intLower, intHigher))
    
    try :
        INTuserGuess = int(input('Please enter your guess: ')) #integer for user guess
    except :

        try :
            INTuserguess = int(input('There was an error! Please enter a whole number from the range {0} - {1}\
            '.format(intLower, intHigher)))
        except :
            print('Sorry, there was an error.')
            clearConsole(2)
            gameMenu()

    rndNumber = randomNumber(intLower, intHigher)

    while INTuserGuess != rndNumber : 
        print("\nSorry, you didn't guess the number")

        if INTuserGuess < rndNumber :
            print('Your guess was low')

            try : 
                INTuserGuess = int(input("\nWhat's your next guess? "))
            except : 
                try : 
                    INTuserguess = int(input('\nSorry, there was an error; please try again: '))
                except :
                    print('Sorry, there was an error.')
                    clearConsole(2)
                    gameMenu()
                 

        if INTuserGuess > rndNumber :
            print('Your guess was high')

            try : 
                INTuserGuess = int(input("What's your next guess? "))
            except : 
                try : 
                    INTuserguess = int(input('\nSorry, there was an error; please try again: '))
                except :
                    print('Sorry, there was an error.')
                    clearConsole(2)
                    gameMenu()

    print('\n\nCongratulations! you guessed the number.')
    print('Returning you to the menu...')
    clearConsole(3)
    gameMenu()


def randomNumber(a, b) :
    #Generates a random int from range a, b

    return(randint(a,b))

def cls(): 
  print ("\n" * 100)

def clearConsole(wait) : #function to clear console on Linux or Windows

    #Clears console, with optional time delay. Will attempt to clear the console for Windows, should that fail it will attempt to clear the console for Linux.
    

    import time
    time.sleep(wait) 
    # produces a delay based on the argument given to clearConsole()
    
    import os

    try :
       os.system(cls) #clears console on Windows

    except :
       os.system('clear') #clears console on Linux


def main() : 
    gameMenu()

if __name__ == "__main__" :
    main()