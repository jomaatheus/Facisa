#Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('digite o valor '))
numero2 = int(input('digite o valor '))

if numero1 > numero2:
    print(numero1,'maior')
elif numero1 < numero2:
    print(numero2,'maior')
else:
    print('Iguais')