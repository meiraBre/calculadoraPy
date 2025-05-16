from Calculadora.operacoes import Calculadora

def test_dividir_numeros_com_input ():
    calc = Calculadora()
    actual_result = calc.dividir_numeros (num1 = 9, num2 = 9)
    assert actual_result == 1 
    if actual_result == True:
        print("Teste realizado com sucesso!")