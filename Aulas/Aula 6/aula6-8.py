# exemplo 8 (possivel cagada de vcs)

opcao = 0
while opcao != 5:
    print('1) List, 2) Add, 3) Del, 4) Search, 5) Leave')    
    opcao = input('Digite a sua opcao ')
    
    if opcao == 1:
        print('Listar')
    elif opcao == 2:
        print('Adicionar')
    elif opcao == 3:
        print('Del')
    elif opcao == 4:
        print('Search')
    elif opcao != 5:
        print('Opcao Invalida')

print('Saindo')
     