from Calculadora.operacoes import Calculadora

def test_multiplicar_numeros_com_input ():
    calc = Calculadora()
    actual_result = calc.multiplicar_numeros (num1 = 9, num2 = 9)
    assert actual_result == 81