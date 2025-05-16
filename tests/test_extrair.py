import pytest
from Calculadora.operacoes import Calculadora

@pytest.mark.parametrize("num1, resultado", [
    (72, pytest.approx(8.48528137423857)),
    (25, 5),
    (121, 11),
])
#Utilização de IA para ver essa função de aproximar valores (pytest.approx)

def test_extrair_raiz_quadrada_numeros_com_input (num1, resultado):
    calc = Calculadora()
    actual_result = calc.extrair_raiz_quadrada (num1)
    assert actual_result == resultado
    
@pytest.mark.parametrize("num1", [-12])
def test_extrair_raiz_quadrada_com_valor_invalido(num1):
    calc = Calculadora()
    with pytest.raises(ValueError):
        calc.extrair_raiz_quadrada(num1)