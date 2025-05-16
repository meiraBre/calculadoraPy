from Calculadora.operacoes import Calculadora

def test_subtrair_numeros_com_input ():
    calc = Calculadora()
    actual_result = calc.subtrair_numeros (num1 = 9, num2 = 9)
    assert actual_result == 0 