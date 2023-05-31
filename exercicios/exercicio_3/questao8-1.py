#• Faça um Programa que leia três números e mostre-os em ordem decrescente.

number1=int(input('digite um numero A: '))

number2=int(input('digite um numero B: '))

number3=int(input('digite um numero C: '))


ordems=[]

ordems.append(number1)
ordems.append(number2)
ordems.append(number3)

ordems.sort()

for ordem in ordems:
    print(ordem)
