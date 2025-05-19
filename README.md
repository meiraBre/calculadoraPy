# 🗃Calculadora em Python e testes com Pytest
[Link do repositorio](https://github.com/meiraBre/calculadoraPy)
(Trabalho realizado durante o estágio de QA na Compass)

## 🧰 Técnicas e ferramentas utilizadas:
- Linguagem: Python
- Framework: Pytest
- Parametrização de testes: uso do @pytest.mark.parametrize para testar múltiplos valores de entrada com menos código e mais cobertura.
- Validação de exceções: testes com pytest.raises para garantir tratamento correto de erros.

## 🛠 Operações básicas + duas operações de minha escolha
- Soma
- Subtração
- Divisão
- Multiplicação
- Potenciação
- Raiz quadrada

### 📝 Utilização de TDD (Test Driven Development - Desenvolvimento guiado por testes)
 Criação de Testes unitários antes da implementação de métodos da calculadora.

## 🔎 Cobertura de testes
🔢 Operações testadas:
- Soma ✅
- Subtração ✅
- Multiplicação ✅
- Divisão ✅
- Potenciação ✅
- Raiz quadrada ✅
- ✔ Total: 6 de 6 operações cobertas

⚠️ Testes de exceção:
- Divisão por zero ✅
- Raiz quadrada de número negativo ✅
- ✔ Total: 2 de 2 exceções tratadas
