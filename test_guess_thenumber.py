from main import main
from unittest.mock import patch

def test_guess():
    # Establecer el valor esperado del numero aleatorio
    expected_number = 52
    #Usas patch para simular la generación del numero aleatorio
    with patch('random.randint', return_value=expected_number):
        # Llamo a main que debe generar el numero aleatorio
        generated_number = main()
        #Verificar si el numero generado es igual al esperado 
    assert generated_number == expected_number