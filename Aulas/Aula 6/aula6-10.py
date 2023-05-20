
# exemplo 10 - sistema v1 COMPLETO

opcao = 0
filmes = [ ]

while opcao != 5:
    print('1) List, 2) Add, 3) Del, 4) Search, 5) Leave')    
    opcao = int(input('Digite a sua opcao '))
    
    if opcao == 1:

        if len(filmes) == 0:
            print('Nao existem filmes a serem listados!')
        else:
            print('Lista de Filmes')
            for item in filmes:
                print('-',item)

    elif opcao == 2:
        
        novoFilme = input('Digite o nome do filme ')
        filmes.append(novoFilme)
        print('Filme adicionado com sucesso!')
    elif opcao == 3:
        print('Del')
    elif opcao == 4:
        print('Search')
    elif opcao != 5:
        print('Opcao Invalida')

print('Saindo')
    