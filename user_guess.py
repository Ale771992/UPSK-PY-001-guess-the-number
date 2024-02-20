def user_guess(aleatory_number, guessed_user):
    # Con input le pedimos al usuario que ingrese un numero y se usa int para convertir la entrada a numero entero.
    guessed_user = False
    guess_user = int(input("Guess a number between 1 and 100: ----> "))
    print("Your guess is: ", guess_user)
    if guess_user == aleatory_number:
       print("Congratulations, you guest the number!")
       guessed_user = True
    elif guess_user < aleatory_number:
       print("Your numer is to small, try again")
    else:
       print("Your numer is too big, try again")
    return guessed_user