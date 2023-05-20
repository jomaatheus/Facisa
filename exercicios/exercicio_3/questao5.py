#• Faça um Programa que leia três números e mostre o maior deles

number1=int(input('digite o primeiro numero: '))
number2=int(input('digite o segundo numero: '))
number3=int(input('digite o terceiro numero: '))

maior_numero = number1

if number2 > maior_numero:
    maior_numero = number2

if number3 > maior_numero:
    maior_numero = number3

print("O maior número digitado é:", maior_numero)