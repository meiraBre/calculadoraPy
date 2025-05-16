import pytest
from Calculadora.operacoes import Calculadora

@pytest.mark.parametrize("num1, num2, resultado",[
    (96, 6, 16),
    (45, 5, 9),
    (18, 3, 6),
    (1500, 1.5, 1000),
])
def test_dividir_numeros_com_input(num1, num2, resultado):
    calc = Calculadora()
    actual_result = calc.dividir_numeros (num1, num2)
    assert actual_result == resultado

def test_divisao_por_zero():
    calc = Calculadora()
    with pytest.raises(ValueError) as exc_info:
        calc.dividir_numeros(10, 0)
    assert str(exc_info.value) == "Não digite zero para realizar a operação de divisão"


# Utilização de IA para me ajudar a elaborar um teste para a exeção de divisão por 0.