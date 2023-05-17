#• Faça um Programa que peça a temperatura em graus Fahrenheit, 
#transforme e mostre a temperatura em graus Celsius.
#• C = 5 * ((F-32) / 9).

grauFah=int(input('digite a temperatura em graus fahrenheit: '))

celcius=5*((grauFah-32/9))
celcius=round(celcius,2)

print('a temperatura em graus Celcius é:',celcius)