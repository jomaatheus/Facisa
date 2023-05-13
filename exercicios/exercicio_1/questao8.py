#8 Faça um programa que pede duas notas de um aluno.
#Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

grade1=float(input('digite sua primeira nota: '))
grade2=float(input('digite sua segunda nota: '))

average=(grade1+grade2)/2

if average >=7 and average< 10:
    print('Aprovado')

elif average == 10:
    print('Aprovado com Distinção')

else:
    print('Reprovado')


'''
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
