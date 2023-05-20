#Faça um Programa que peça dois números e imprima o maior deles.

number1=int(input('digite o primeiro numero: '))

number2=int(input('digite o segundo numero: '))

if number1 > number2:
    print(number1,'é maior que',number2)
else:
    print(number2,'é maior que', number1)