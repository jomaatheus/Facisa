#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

number=int(input('digite um numero: '))


if number > 0 :
    print(number,'é positivo')

elif number < 0 :
    print(number,'é negativo')

else:
    print('nulo')