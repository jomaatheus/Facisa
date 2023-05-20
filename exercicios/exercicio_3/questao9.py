#Faça um Programa que pergunte em que turno você estuda. 
#Peça para digitar M-matutinoou V-Vespertinoou N-Noturno. Imprima a
#mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('digite seu turno aqui: ')
turno = turno.lower()

if turno == 'm':
    print('Bom Dia!')

elif turno == 'v':
    print('Boa Tarde!')

elif turno == 'n':
    print('Boa Noite!')

else:
    print('Valor Inválido')

