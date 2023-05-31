'''
• Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.

'''

opcao=1

while opcao != 2:
    print('1) numero 2) sair')
    print()
    opcao=int(input('digite uma opção: '))
    print()
    print('opção lida',opcao)

    if opcao == 1:
        print()
        number=input('digite um numero: ')
        print()

        if '.' in number:
            flaotNumber=float(number)
            print (number,'é decimal')
            print()
            
        elif number.isdigit():
            print(number, 'é inteiro')
            print()
        else:
            print('Opção inválida. Por favor, digite um número válido.')
            print()
    
    if opcao == 2:
        print()
        print('é o jao')
            
    