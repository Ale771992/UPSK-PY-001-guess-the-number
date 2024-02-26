import random
from colorama import init, Fore
def computer_guess(aleatory_number):
    guess_computer = random.randint(1,100)
    guessed_computer = False
    print(Fore.LIGHTGREEN_EX + "The computer's guess is: ", guess_computer)
    if guess_computer == aleatory_number:
           print (guess_computer)
           print("Sorry, your computer guessed the number")
           guessed_computer = True
    elif guess_computer < aleatory_number:
           print("The computer's guess is too small ")
    else:
           print("The computer's guess is too big")
    return guessed_computer