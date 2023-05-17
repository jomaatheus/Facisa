# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celcius=int(input('digite a temperatura em graus Celcius: '))

grauFah=celcius*9/5+32
grauFah=round(grauFah,2)

print('a temperatura em graus Fahrenheit é:',grauFah)