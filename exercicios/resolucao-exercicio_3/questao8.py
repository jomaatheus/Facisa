#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = [ ]
numeros.append(8)
numeros.append(4)
numeros.append(3)
numeros.append(120)

print('Antes')
for numero in numeros:
    print(numero)

numeros.sort(reverse=True)

print('Depois')
for numero in numeros:
    print(numero)