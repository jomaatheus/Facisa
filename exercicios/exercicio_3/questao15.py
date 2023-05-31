'''
Faça um Programa que peça 
um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
'''

number=int(input('digite um numero inteiro: '))

if number % 2 != 0:
    print(number, 'é impar')
elif number == 0:
    print(number, 'é neutro')
else:
    print(number,'é par')