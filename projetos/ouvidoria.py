menu=[]
opcao=1 #numero qualquer para entrar em while

while opcao !=5: #cria um menu
    print()
    print('='*30)
    print('\n Opção 1) Cadastrar ocorrências')
    print('\n Opção 2) Listar ocorrências')
    print('\n Opção 3) Apagar ocorrências')
    print('\n Opção 4) Consultar por código')
    print('\n Opção 5) Sair')
    print()
    print('='*30)
    print()
    opcao=int(input('digite uma opção: '))
    print()
    print('opção lida',opcao)
    print()

    if opcao == 1:
        
        ocorrencia = input('Digite sua ocorrencia: ')
        
        if ocorrencia.strip():  # Verifica se a string não está vazia após remover os espaços em branco
            menu.append(ocorrencia)
            print()
            print('Ocorrencia salva com sucesso!!')
        else:
            print()
            print('Erro: A ocorrencia não pode estar vazia.')

    
    elif opcao == 2:
        if menu: #verifica se o menu ta vazio ou se há alguma ocorrencia
            for i in range(len(menu)): #numera as ocorrencias
                print('Ocorrencia Numero',i+1,':', menu[i])
            
        else:   
            print('Não há ocorrencias.')
    
    elif opcao == 3:

        print('Ocorrencias disponiveis: ')
        print()

        for i in range(len(menu)): # numera as ocorrencias
                    print('Ocorrencia Numero',i+1,':', menu[i])
                    print()

        if menu: #verifica se há ou não ocorrencias
                 
            apagarOcorrencia=int(input('Digite o Numero da ocorrencia: ')) 
            apagarOcorrencia = menu.pop(apagarOcorrencia-1) # se houver ocorrencia, escolher e apagar
            print()
            print('Ocorrencia apagada com sucesso!')

        else:
            print("Não há ocorrencias.")
    
    elif opcao == 4:

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
            print('Não há ocorrências.')
            

    elif opcao == 5:
         print('Obrigado(a), pela preferência espero ter ajudado!!')
         print()
    
    elif opcao != 5: #qualquer opção diferente de 5 ta invalida.
         print('(Opção invalida)')
         print()
         print('Selecione uma opção valida: ')

    