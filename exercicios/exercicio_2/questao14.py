'''
João Papo-de-Pescador, homem de bem, 
comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
de R$ 4,00 por quilo excedente.
 João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da 
multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''

limitePeso=50

pesoPeixes= float(input('digite o peso dos peixes em quilos: '))

if pesoPeixes > limitePeso:
    excesso= pesoPeixes-limitePeso
    multa=excesso*4.00
    print("Peso excedente de", excesso, "quilos")
    print("Multa a ser paga: R$", multa)
else:
    excesso = 0
    multa = 0
    print("Peso dentro do limite, sem multa a pagar.")