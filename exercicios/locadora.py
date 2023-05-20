filmes=['As vantagens de ser invisivel', 'Ocean waves', 'i want to eat your pancreas']
opcao=5

while True:
    print('opção 1) listar os filmes')
    print('opção 2) devolver um filme')
    print('opção 3) alugar um filme')
    print('opção 4) sair')
    
    opcao=int(input('digite uma opção: '))
    print('opção lida',opcao)

    if opcao == 1:
    
        for i in range(len(filmes)):
            print(i+1, '- filme:',filmes[i])

    elif opcao == 2:

        filmeDevolvido=input('digite o nome do filme devolvido: ')
        filmes.append(filmeDevolvido)

    elif opcao == 3:


        print('filmes disponiveis')
        for i in range(len(filmes)):
            print(i+1, 'filme:',filmes[i])

        filmeAlugado=int(input('digite o numero do filme: '))
        filmes.pop(filmeAlugado-1)
        #pop remove um elemento/item da lista
        print('filme alugado com sucesso')
    
    elif opcao >=4:
        break