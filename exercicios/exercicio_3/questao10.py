#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
#(1-Domingo, 2-Segunda, etc.), se digitar outro valor deve aparecer valor inválido

semana=['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']
numero=int(input('Digite um numero de 1 a 7: '))

if numero >= 1 and numero <= 7:
    diaSemana = semana[numero - 1]
    print ('O dia correspondente ao número', numero , 'é' , diaSemana,'.')
else:
    print('Valor inválido. O número deve ser de 1 a 7.')