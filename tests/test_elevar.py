from Calculadora.operacoes import Calculadora

def test_elevar_numeros_com_input ():
    calc = Calculadora()
    actual_result = calc.elevar_numeros (num1 = 2, num2 = 3)
    assert actual_result == 8