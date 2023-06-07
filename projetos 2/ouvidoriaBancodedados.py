from operacoesbd import *

menu=[]
opcao=1 #numero qualquer para entrar em while
conexao = abrirBancoDados('localhost','root','12345','ouvidoria')

while opcao != '6': #cria um menu
    print()
    print('='*40)
    print('\n Opção 1) Cadastrar ocorrências')
    print('\n Opção 2) Listar ocorrências')
    print('\n Opção 3) Apagar ocorrências')
    print('\n Opção 4) Consultar por código')
    print('\n Opção 5) Alterar ocorrências')
    print('\n Opção 6) Sair')
    print()
    print('='*40)
    print()
    opcao=input('digite uma opção: ')
    print()
    print('opção lida:',opcao)
    print()

    if opcao == '1':
        assunto = input('Digite o assunto da raclamação: ')
        detalhes = input('\nDigite os detalhes da reclamação: ')
        aut = input('\nDigite o nome de quem deseja fazer a reclamação: ')

        sqlInsercao = 'insert into menu (Título,Detalhe,Autor) values(%s,%s,%s)'
        valores = (assunto, detalhes, aut)

        insertNoBancoDados(conexao, sqlInsercao, valores)
    
    elif opcao == '2':
        print('Listagem de Reclamações')
        consultaListagem = 'select * from menu'
        menu = listarBancoDados(conexao, consultaListagem)

        for fi in menu:
            print('| Código: ', fi[0],'|', '| Título: ', fi[1],'|','| Detalhe: ',fi[2],'|','| Autor:',fi[3],'|', '| Data: ', fi[4],'|')
    
    elif opcao == '3':  

        codigo = input('Digite o codigo da reclamação: ')
        consultaListagem = 'delete from menu where Código = %s '
        dados = (codigo,)

        excluirBancoDados(conexao, consultaListagem, dados)

    
    elif opcao == '4':

        codigo = input('Digite o codigo da raclamação: ')
        consultaListagem = 'select * from menu where Código = ' + codigo

        menu = listarBancoDados(conexao, consultaListagem)

        for fi in menu:
            print('| Código: ', fi[0],'|', '| Título: ', fi[1],'|','| Detalhe: ',fi[2],'|','| Autor:','|',fi[3], '| Data: ', fi[4])

            
    elif opcao == '5':
        
        codigo = input('Digite o código da reclamação: ')
        novoTitulo = input('\nDigite o assunto da nova reclamação: ')
        novoDetalhe = input('\nDigite os detalhes da reclamação: ')
        aut = input('\nDigite o nome de quem deseja fazer a reclamação: ')

        sqlAtualizar = 'UPDATE menu SET Título = %s, Detalhe = %s, Autor = %s WHERE Código = %s'
        valores = (novoTitulo, novoDetalhe, aut, codigo)

        atualizarBancoDados(conexao, sqlAtualizar, valores)

         

    elif opcao == '6':
         print('='*50)
         print()
         print('Obrigado(a), pela preferência espero ter ajudado!!')
         print()
         print('='*50)

    elif opcao != '6' : #qualquer opção diferente de 5 ta invalida.
         print('(Opção invalida)')
         print()
         print('Selecione uma opção valida: ')

encerrarBancoDados(conexao)
print('Obrigado por usar nossa ouvidoria!')
    