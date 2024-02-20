from user_guess import user_guess
from computer_guess import computer_guess
import random

def main():
    aleatory_number = random.randint(1, 100)
    round_number = 1
    """ Inicializo la variable guessed como falsa, de lo contrario si se establece como verdadera desde el inicio,
        el bucle nunca empezaria porque la usuaria ya adivino, porque guessed es true. """
    guessed_user = False
    guessed_computer = False
    user_attemps = 0
    computer_attemps = 0

    while not guessed_user and not guessed_computer:
        print(f"Round {round_number}") # Con la f indicas que se permite la interpolación de variables dentro del texto.

        # User's turn 
        guessed_user = user_guess(aleatory_number, guessed_user)
        user_attemps += 1
       
        
        #Computer's turn
        if not guessed_user:
           guess_computer = computer_guess(aleatory_number)
           computer_attemps += 1
           round_number += 1
          

    print(f"Total guesses from you {user_attemps}")
    print(f"Total guesses from the computer {computer_attemps}")

# la expresion se utiliza para determinar si un archivo de script se está ejecutando directamente o si ha sido importado como un módulo en otro script
if __name__ == "__main__":
    main()

