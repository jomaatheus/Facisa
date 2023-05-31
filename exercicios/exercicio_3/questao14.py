opcao = 1
print(30 * '=')
print('Seja bem-vindo!!')

while opcao != 2:
    print(30 * '=')
    print()
    print('1) Saque 2) Sair')
    print()
    print(30 * '=')
    print()

    opcao = int(input('Digite uma opção: '))
    print('Opção lida:', opcao)

    if opcao == 1:
        print('\nAs notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.')
        print('\nO valor mínimo é de 10 reais e o máximo é de 600 reais.')
        print()

        valor = int(input('Qual o valor do saque? '))

        if valor < 10 or valor > 600:
            print("Valor inválido.")
        else:
            cemReais = valor // 100
            valor %= 100
            cinquentaReais = valor // 50
            valor %= 50
            dezReais = valor // 10
            valor %= 10
            cincoReais = valor // 5
            umReal = valor % 5

            resultado = ""
            if cemReais > 0:
                resultado += str(cemReais) + " nota(s) de 100 reais, "
            if cinquentaReais > 0:
                resultado += str(cinquentaReais) + " nota(s) de 50 reais, "
            if dezReais > 0:
                resultado += str(dezReais) + " nota(s) de 10 reais, "
            if cincoReais > 0:
                resultado += str(cincoReais) + " nota(s) de 5 reais, "
            if umReal > 0:
                resultado += str(umReal) + " nota(s) de 1 real."

            print(resultado)

    if opcao == 2:
        print('Obrigado(a) pela escolha')
