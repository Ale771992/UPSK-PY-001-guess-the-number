from colorama import init, Fore
def user_guess(aleatory_number, guessed_user):
    # Con input le pedimos al usuario que ingrese un numero y se usa int para convertir la entrada a numero entero.
    guessed_user = False
    # La función int() se encarga de convertir la entrada del usuario, que es inicialmente una cadena de texto (string), en un número entero.
    guess_user = int(input("Guess a number between 1 and 100: ----> "))
    print(Fore.LIGHTGREEN_EX + "Your guess is: ", guess_user)
    if guess_user == aleatory_number:
       print("Congratulations, you guest the number!")
       guessed_user = True
    elif guess_user < aleatory_number:
       print("Your number is to small, try again")
    else:
       print("Your number is too big, try again")
    return guessed_user