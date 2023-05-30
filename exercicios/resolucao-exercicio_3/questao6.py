#usando sum e len together

notas = [ 7, 7, 7, 10 ]
media = sum(notas) / len(notas)
media = round(media,2)
print(media)

# fazendo medias CODIGO PANCADA!!!!!!!!!! Nao chore, Caio!

nota = 0
notas = [ ]

while nota != -1:
    nota = int(input('diz a nota (-1 pra parar)'))
    if nota != -1:
        notas.append(nota)

media = sum(notas) / len(notas)
media = round(media,2)
print('a media foi',media)