'''
• Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu
salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
 8% para o INSS e 5% para o sindicato, faça um
programa que nos dê:
• salário bruto.
• quanto pagou ao INSS.
• quanto pagou ao sindicato.
• o salário líquido.
• calcule os descontos e o salário líquido, conforme a tabela à direita
'''

hora=float(input('digite quanto você ganha por horas trabalhadas: '))
horaMes=float(input('digite quantas horas você trabalhou no mês: '))

salario=hora*horaMes

impostoRenda=salario*0.11

inss=salario*0.08

sindicato=salario*0.05

salarioBruto=salario

salarioLiquido=salario-impostoRenda-inss-sindicato

print("Salário Bruto: R$", salarioBruto)
print("Desconto Imposto de Renda (11%): R$", impostoRenda)
print("Desconto INSS (8%): R$", inss)
print("Desconto Sindicato (5%): R$", sindicato)
print("Salário Líquido: R$", salarioLiquido)