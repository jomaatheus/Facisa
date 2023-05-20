# exemplo 1 (listar os filmes)

filmes = [ 'lagoa azul', 'titanic', 'crepusculo' ] 

if len(filmes) == 0:
    print('Nao existem filmes a serem listados!')
else:
    print('Lista de Filmes')
    for item in filmes:
        print('-',item)
