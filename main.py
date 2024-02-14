import random #Importo el modulo random, que se usa para generar numeros aleatorios, de la biblioteca de Pyton 
# Genero un numero aleatorio con la funcion randit del modulo random
aleatory_number = random.randint(1, 100)
""" Inicializo la variable guessed como falsa, de lo contrario si se establece como verdadera desde el inicio,
el bucle nunca empezaria porque la usuaria ya adivino, porque guessed es true. """
guessed_user = False
guessed_computer = False

# Implemento el bucle para que la jugadora adivine el numero: "Mientras no se haya adivinado el numero"
while not guessed_user:
# Con input le pedimos al usuario que ingrese un numero y se usa int para convertoir la entrada a numero entero.
   guess = int(input("Guess a number between 1 and 100"))

   if guess == aleatory_number:
       print("Congratulations, you guest the number!")
       guessed = True
   elif guess < aleatory_number:
       print("Your numer is to small, try again")
   else:
       print("Your numer is too big, try again")
