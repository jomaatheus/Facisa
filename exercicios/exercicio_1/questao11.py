#11 As Organizações Hamurabi Medeiros resolveram dar um aumento de salário aos seus colaboradores 
#e lhe contrataram para desenvolver o programa que calculará os reajustes.

salary=float(input('Digite o seu salario: '))

if salary <= 280:
    adjustment=20

elif salary > 280 and salary < 700:
    adjustment=15

elif salary >=700 and salary <= 1500:
    adjustment=10

else:
    adjustment=5



increase= salary*adjustment/100

newSalary=salary+increase

print("Salário antes do reajuste: R$",salary)
print("Percentual de aumento aplicado:",adjustment,'%')
print("Valor do aumento: R$",increase)
print("Novo salário após o aumento: R$",newSalary)



'''
• Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
• salários até R$ 280,00 (incluindo) : aumento de 20%
• salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
• salários de R$ 1500,00 em diante : aumento de 5%
• Após o aumento ser realizado, informe na tela:
• o salário antes do reajuste;
• o percentual de aumento aplicado;
• o valor do aumento;
• o novo salário, após o aumento
'''
