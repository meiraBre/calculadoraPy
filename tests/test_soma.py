from Calculadora.operacoes import Calculadora

def test_somar_numeros_soma_com_input ():
    calc = Calculadora()
    actual_result = calc.somar_numeros (num1 = 8, num2 = 2)
    assert actual_result == 10