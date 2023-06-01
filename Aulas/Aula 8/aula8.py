#Exemplo para Debug
filmes = [ ]
opcao = 1

while opcao != 3:
    print('locadora de Caio! 1 list 2 add 3 leave')
    opcao = int(input('digite a opcao: '))

    if opcao == 1:
        for filme in filmes:
            print(filme)
    elif opcao == 2:
        novoFilme = input('digite o nome do filme ')
        filmes.append(novoFilme)
        print('Filme adicionado')

print('Fim!')
