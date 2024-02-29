import unittest
import random
from unittest.mock import patch
from user_guess import user_guess
from computer_guess import computer_guess

# unittest contains both a testing framework and a test runner
# class se usa para definir un "molde" que contendra metodos de prueba
class TestAleatoryNumber(unittest.TestCase):#TestCase es una clase dentro de unittest que te da funcionalidades y metodos para escribir tus pruebas. 
 def test_random_number(self): # debes incluir el parámetro self, es necesario para acceder a las aserciones y otros métodos proporcionados por la clase TestCase.
  
  generated_number = random.randint(1, 100)
  
  self.assertGreaterEqual(generated_number, 1)
  self.assertLessEqual(generated_number, 100)

# Test para cuando el usuario adivina
class TestUserGuess(unittest.TestCase):
 @patch('builtins.input', return_value ='50')
 def test_guessuser_correct(self, mock_input):
   aleatory_number = 50
   guessed_user = False
   self.assertTrue(user_guess(aleatory_number, guessed_user))

 @patch('builtins.input', return_value = '25')
 def test_guessuser_incorrect(self, mock_input):
   aleatory_number = 50
   guessed_user = False
   self.assertFalse(user_guess(aleatory_number, guessed_user))


#Test para cuando la computadora falla
class TestComputerGuess(unittest.TestCase):
  @patch('builtins.input', return_value = '25')
  def test_guesscomputer_incorrect(self, mock_input):
   aleatory_number = 50
   guessed_computer = False
   self.assertFalse(computer_guess(aleatory_number))
                           
if __name__=='__main__':
   unittest.main()

    # unittest requires that: You put your tests into classes as methods and
    # You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement