import pytest
from Calculadora.operacoes import Calculadora

@pytest.mark.parametrize("num1, num2, resultado", [
    (21, 3, 63),
    (40, 2, 80),
    (6, 6, 36),
    (-5, -5, 25)
])
def test_multiplicar_numeros_com_input (num1, num2, resultado):
    calc = Calculadora()
    actual_result = calc.multiplicar_numeros (num1, num2)
    assert actual_result == resultado