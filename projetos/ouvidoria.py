menu=[]
opcao=1 #numero qualquer para entrar em while

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
        
        ocorrencia = input('Digite sua ocorrencia: ')
        
        if ocorrencia.strip():  # Verifica se a string não está vazia após remover os espaços em branco
            menu.append(ocorrencia)
            print()
            print('Ocorrencia salva com sucesso!!')
        else:
            print()
            print('Erro: A ocorrencia não pode estar vazia.')

    
    elif opcao == '2':
        if menu: #verifica se o menu ta vazio ou se há alguma ocorrencia
            for i in range(len(menu)): #numera as ocorrencias
                print('Ocorrencia Numero',i+1,':', menu[i])
            
        else:   
            print('Não há ocorrencias para listar.')
    
    elif opcao == '3':

        print('Ocorrencias disponiveis: ')
        print()

        for i in range(len(menu)): # numera as ocorrencias
                    print('Ocorrencia Numero',i+1,':', menu[i])
                    print()

        if menu: #verifica se há ou não ocorrencias
                 
            apagarOcorrencia=input('Digite o Numero da ocorrencia: ')
            apagarOcorrencia = int(apagarOcorrencia)

            if 1 <= apagarOcorrencia <= len(menu):
                
                reclamacaoRemovida=menu.pop(apagarOcorrencia-1)
                print()
                print('Ocorrencia apagada com sucesso!')
            else:
                 print()
                 print('Erro: Digite uma ocorrencia valida.')
        else:
            print("Não há ocorrencias para apagar.")
    
    elif opcao == '4':

        if menu:  # Verifica se o menu não está vazio
            
            codigo = int(input('Digite o código da ocorrência: '))

            if codigo > 0 and codigo <= len(menu): #verifica se o codigo é valido/existe de acordo com o menu
                ocorrencia = menu[codigo - 1]
                print('\nOcorrência encontrada:')
                print('\nCódigo:', codigo)
                print('\nOcorrência:', ocorrencia)
            else:
                print('\nCódigo inválido.')
        else:
            print('Não há ocorrências para consultar.')
            
    elif opcao == '5':

        print('Ocorrencias disponiveis: ')
        print()

        for i in range(len(menu)): # numera as ocorrencias
                    print('Ocorrencia Numero',i+1,':', menu[i])
                    print()

        if menu: #verifica se há ou não ocorrencias
                 
            alterarOcorrencia=int(input('\nDigite o Numero da ocorrencia: '))

            if 0 > alterarOcorrencia <= len(menu):
                novaOcorrencia = input('\nDigite a nova descricao da ocorrencia: ')
                menu[alterarOcorrencia-1] = novaOcorrencia
                print('Ocorrencia alterada com sucesso!')
            else:
                print()
                print('Ocorrencia invalida!')             
                
        else:
            print("Não há ocorrencias para alterar.")
         

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

    