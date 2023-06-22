'''
CAIO VICTOR BEZERRA DE MEDEIROS SOUTO
CAIO MOURA PORTELA SOUSA
LARISSA ALCANTARA SIPIAO
SANIEL MARTINS NOBREGA
JONILFO PEREIRA ARAUJO JUNIOR
JOAO MATHEUS DE FIGUEIREDO TAVARES
'''

from ouvidoria import *
from operacoesbd import *
from colorama import Fore, Style


listaReclamacoes = []
conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria2')

opcao = 0
while opcao != 8:
    print()
    print("=" * 40 + Style.RESET_ALL)
    print('Menu')
    print()
    print('1-' + Fore.GREEN + 'Listagem das manifestações' + Style.RESET_ALL)
    print('2-' + Fore.GREEN + 'Listagem de manifestações por tipo' + Style.RESET_ALL)
    print('3-' + Fore.GREEN + 'Criar uma nova manifestação' + Style.RESET_ALL)
    print('4-' + Fore.GREEN + 'Exibir quantidade de manifestações' + Style.RESET_ALL)
    print('5-' + Fore.GREEN + 'Pesquisar uma manifestação por código' + Style.RESET_ALL)
    print('6-' + Fore.GREEN + 'Alterar o título e uma descrição de uma manifestação' + Style.RESET_ALL)
    print('7-' + Fore.GREEN + 'Excluir uma manifestação pelo código' + Style.RESET_ALL)
    print('8-' + Fore.RED + 'Sair do sistema' + Style.RESET_ALL)
    print("=" * 40 + Style.RESET_ALL)
    print()
    opcao = int(input('Digite uma opção: '))
    print()

    if opcao == 1:
        listarreclamacoes(conexao)

    elif opcao == 2:
        listarportipo(conexao)
        
    elif opcao == 3:
        criarmanifestacao(conexao)
        
    elif opcao == 4:
        exibirmanifestacoes(conexao)

    elif opcao == 5:
        pesquisarporcodigo(conexao)
        
    elif opcao == 6:
        alterartitulodescricao(conexao)

    elif opcao == 7:
        excluirmanifestacao(conexao)

    elif opcao == 8:
        print('Obrigado por participar!')

    else:
        print('opcao invalida')

encerrarBancoDados(conexao)