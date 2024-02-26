import unittest
import random
from main import main
from user_guess import user_guess
from computer_guess import computer_guess

# unittest contains both a testing framework and a test runner
# class se usa para definir un "molde" que contendra metodos de prueba
class TestGuess(unittest.TestCase):#TestCase es una clase dentro de unittest que te da funcionalidades y metodos para escribir tus pruebas. 
 def test_random_number(self): # debes incluir el parámetro self, es necesario para acceder a las aserciones y otros métodos proporcionados por la clase TestCase.
  
  generated_number = random.randint(1, 100)
  
  self.assertGreaterEqual(generated_number, 1, "Generated numero is too small")
  self.assertLessEqual(generated_number, 100, "Generated number is too big")
# Test para cuando el usuario adivina
 def test_guessuser_correct(self):
   aleatory_number = 50
   guessed_user = True
   result = user_guess(aleatory_number, guessed_user)
   print(result)
   self.assertTrue(result)

#Test para cuando la computadora falla
 def test_guesscomputer_incorrect(self):
   aleatory_number = 50
   result = computer_guess(aleatory_number)
   print(result)
   self.assertFalse(result)
                           
if __name__=='__main__':
    unittest.main()

    # unittest requires that: You put your tests into classes as methods and
    # You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement