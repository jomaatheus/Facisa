#12 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
# ao longo de um semestre, e calcule a sua média.
#A atribuição de conceitos deve obedecer à tabela acima.

grade1=float(input('Digite sua primeira nota: '))
grade2=float(input('Digite sua segunda nota: '))


average=(grade1+grade2)/2

if average >=9 and average <=10:
    concept="A"

elif average >=7.5 and average <=9:
    concept="B"

elif average >=6 and average <=7.5:
    concept="C"

elif average >=4 and average <=6:
    concept="D"

else:
    concept="E"   

print("A média do aluno é: ", average)
print("O conceito do aluno é: ", concept)

'''
Média Conceito
Entre 9 e 10 A
Entre 7.5 e 9 B
Entre 6 e 7.5 C
Entre 4 e 6 D
Entre 0 e 4 E

'''