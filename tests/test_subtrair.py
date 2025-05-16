import pytest
from Calculadora.operacoes import Calculadora

@pytest.mark.parametrize("num1, num2, resultado",[
    (55, 13, 42),
    (134, 32, 102),
    (21, 34, -13),
    (100, 76, 24)
])

def test_subtrair_numeros_com_input (num1, num2, resultado):
    calc = Calculadora()
    actual_result = calc.subtrair_numeros (num1, num2)
    assert actual_result == resultado