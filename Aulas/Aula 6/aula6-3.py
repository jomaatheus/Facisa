# exemplo 3 codigo CAGADO do menu em LOOP INFINITO

print('1) List, 2) Add, 3) Del, 4) Search, 5) Leave')
opcao = int(input('Digite a sua opcao '))

while opcao != 5:
    if opcao == 1:
        print('Listar')
    elif opcao == 2:
        print('Adicionar')
    elif opcao == 3:
        print('Del')
    elif opcao == 4:
        print('Search')

print('Saindo')
    