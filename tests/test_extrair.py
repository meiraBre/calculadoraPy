from Calculadora.operacoes import Calculadora

def test_extrair_raiz_quadrada_numeros_com_input ():
    calc = Calculadora()
    actual_result = calc.extrair_raiz_quadrada (num1 = 4)
    assert actual_result == 2