import pytest
from Calculadora.operacoes import Calculadora

@pytest.mark.parametrize("num1, num2, resultado", [
    (19, 24, 43),
    (100, 56, 156),
    (-19, 20, 1),
    (34, -20, 14)
])
def test_somar_numeros_soma_com_input (num1, num2, resultado):
    calc = Calculadora()
    actual_result = calc.somar_numeros (num1, num2)
    assert actual_result == resultado