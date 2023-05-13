'''
• Podemos no mesmo IF ou ELIF avaliar duas ou mais expressões
com uso do AND e do OR. Nesta seção, apresentaremos o AND.
• Para melhor entendimento, vamos criar um programa que leia
duas notas de um aluno e:
• Apresente ‘Reprovado’, caso a média seja inferior a 7
• Apresente ‘Aprovado’, caso a média seja maior que 7
• Em casos de média 10, apresente ‘Aprovado com
Distinção’
• Teoricamente, o primeiro pensamento é criar algum dos 2
programas abaixo. Entretanto, se você tiver a média 10, não
será apresentado ‘Aprovado com Distinção’, mas ‘Aprovado’,
por que?

'''

nota1= float(input('digite a nota 1: '))

nota2= float(input('digite a nota 2: ')) 

media= (nota1+nota1)/2

if media < 7:
    print('Reprovado')

elif media >= 7 and media < 10:
    print('Aprovado')

elif media == 10:
    print('Aprovado com distinção')

