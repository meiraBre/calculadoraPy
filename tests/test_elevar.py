import pytest
from Calculadora.operacoes import Calculadora

@pytest.mark.parametrize("num1, num2, resultado",[
    (20, 2, 400),
    (2, 3, 8),
    (15, 1, 15),
    (9, 0, 1) 
])

def test_elevar_numeros_com_input (num1, num2, resultado):
    calc = Calculadora()
    actual_result = calc.elevar_numeros (num1, num2)
    assert actual_result == resultado