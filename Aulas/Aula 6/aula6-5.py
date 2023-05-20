# exemplo 5 (menu funcionando. mas o menu so exibe 1x e nao trata numeros como 6,7

print('1) List, 2) Add, 3) Del, 4) Search, 5) Leave')

opcao = 0
while opcao != 5:
    
    opcao = int(input('Digite a sua opcao '))
    
    if opcao == 1:
        print('Listar')
    elif opcao == 2:
        print('Adicionar')
    elif opcao == 3:
        print('Del')
    elif opcao == 4:
        print('Search')

print('Saindo')