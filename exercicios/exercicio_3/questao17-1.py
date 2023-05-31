numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Qual operação você deseja realizar? (+ para adição, - para subtração, * para multiplicação, / para divisão): ")

if operacao == '+':
    resultado = numero1 + numero2
    print("O resultado da adição é: ", resultado)
elif operacao == '-':
    resultado = numero1 - numero2
    print("O resultado da adição é: ", resultado)
elif operacao == '*':
    resultado = numero1 * numero2
    print("O resultado da adição é: ", resultado)
elif operacao == '/':
    resultado = numero1 / numero2
    print("O resultado da adição é: ", resultado)
else:
    print("Operação inválida.")

# Verificando se o número é par ou ímpar
if resultado % 2 == 0:
    print("O resultado é um número par.")
else:
    print("O resultado é um número ímpar.")

# Verificando se o número é positivo ou negativo
if resultado > 0:
    print("O resultado é um número positivo.")
elif resultado < 0:
    print("O resultado é um número negativo.")
else:
    print("O resultado é zero.")

# Verificando se o número é inteiro ou decimal
if resultado.is_integer():
    print("O resultado é um número inteiro.")
else:
    print("O resultado é um número decimal.")
