'''
• Dentre as operações mais comuns com Strings, são a de tornar
uma string em maiúscula, minúscula ou substituir um dado
caractere por outro. Um exemplo das 3 operações é
apresentado a seguir:
• Na linha 3, colocamos ‘João’ em maiúsculo
• Na linha 6, em minúsculo
• Na linha 9, substituímos o caractere ‘J’ de João por
‘r’, tornando-o ‘Roão’

'''

nome='João'

nome=nome.upper()
print(nome)

nome=nome.lower()
print(nome)

nome=nome.replace('j','r')
print(nome)