#• Faça um Programa que leia três números e mostre o maior e o menor deles.

number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))

maior_numero = number1
menor_numero = number1

if number2 > maior_numero:
    maior_numero = number2
elif number2 < menor_numero:
    menor_numero = number2

if number3 > maior_numero:
    maior_numero = number3
elif number3 < menor_numero:
    menor_numero = number3

print('O maior número é:', maior_numero)
print('O menor número é:', menor_numero)
