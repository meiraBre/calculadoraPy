class Calculadora:
    def somar_numeros (self, num1, num2):
        return num1 + num2

    def subtrair_numeros (self, num1, num2):
        return num1 - num2

    def dividir_numeros (self, num1, num2):
        if num2 == 0:
            raise ValueError("Não digite zero para realizar a operação de divisão") 
        return num1 / num2

    def multiplicar_numeros (self, num1, num2):
        return num1 * num2
    
    def elevar_numeros (self, num1, num2):
        return num1 ** num2

    def extrair_raiz_quadrada (self, num1):
        if num1 < 0 :
            raise ValueError("Não é possível realizar contas de raiz quadrada com número negativo")
        return num1 ** 0.5
#Utilização de IA para fazer a função de raiz quadrada