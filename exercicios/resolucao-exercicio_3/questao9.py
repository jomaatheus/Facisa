#Faça um Programa que peça uma data no formato dd/mm/aaaae determine se a mesma é uma data válida

#data = input('Digite a data: DD/MM/YYYY ')

data = '01/02/2023'

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

if dia < 1 or dia > 31:
    print('dia cagado')

if mes < 1 or mes > 12:
    print('mes cagado')
    
if ano < 1:
    print('ano cagado')
    
#Faça um Programa que peça uma data no formato dd/mm/aaaae determine se a mesma é uma data válida

#data = input('Digite a data: DD/MM/YYYY ')
data = '01/02/2023'

pedacosData = data.split('/')

dia = int(pedacosData[0])
mes = int(pedacosData[1])
ano = int(pedacosData[2])

if dia < 1 or dia > 31:
    print('dia cagado')

if mes < 1 or mes > 12:
    print('mes cagado')
    
if ano < 1:
    print('ano cagado')