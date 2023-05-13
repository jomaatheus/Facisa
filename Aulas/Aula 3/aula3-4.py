'''
Usamos o ELIF (Else IF) para informar uma nova condição a
ser testada, caso a primeira condição (no IF) for falsa. O
funcionamento é apresentado a seguir.

'''

idade=(int(input('digite sua idade: ')))

if idade == 18:
    print('maior de idade')

elif idade <18:
    print('menor de idade')

else:
    print('ja pode ser avô')


'''
Com base na imagem acima, caso a idade for EXATAMENTE
18, as linhas 1,2,5 e 6 são executadas
• Caso a idade seja menor que 18 (ou seja, 17, 16, ...), as
linhas executadas serão as 7,8,5 e 6
• Por fim, caso a idade seja maior de 18 (uma vez que 18 é
atendida no IF, menor que 18 é atendida no ELIF), as linhas
executadas serão 3,4,5 e 6

'''
