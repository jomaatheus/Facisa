#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

hora=float(input('digite quanto você ganha por hora: '))

horaTrabalhada=float(input('digite quantas horas você trabalha no mês: '))

dias=int(input('digite os dias que você trabalhou no mês: '))

salario=hora*horaTrabalhada*dias

print("Seu salario é:",salario)