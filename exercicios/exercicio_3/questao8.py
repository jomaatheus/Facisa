#• Faça um Programa que leia três números e mostre-os em ordem decrescente.

number1=int(input('digite o primeiro numero: '))

number2=int(input('digite o segundo numero: '))

number3=int(input('digite o terceiro numero: '))

maiorNumero=number1
menorNumero=number1

if number2 > maiorNumero:
    maiorNumero = number2
elif number2 < menorNumero:
    menorNumero = number2

if number3 > maiorNumero:
    maiorNumero = number3
elif number3 < menorNumero:
    menorNumero = number3
    
intermediario = number1

if number2 != maiorNumero and number2 != menorNumero:
    intermediario = number2
elif number3 != maiorNumero and number3 != menorNumero:
    intermediario = number3

print('os numeros em ordem decrescente são', menorNumero,intermediario,maiorNumero)



