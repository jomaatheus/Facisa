'''

• Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
 O resultado da operação deve
ser acompanhado de uma frase que diga se o número é:
• par ou ímpar;
• positivo ou negativo;
• inteiro ou decimal.

'''

opcao=1

while opcao != 4:
    print()
    operacoes=['1)Par ou Impar','2)Positivo ou Negativo','3)Inteiro ou Decimal','4)Sair']
    for operacao in operacoes:
        print(operacao)
    print()
    opcao=int(input('digite uma opção: '))
    print()
    print('opção lida',opcao)

    if opcao == 1:
        
        print()
        number1=int(input('digite um numero A: '))
        number2=int(input('digite um numero B: '))
        print()

        if number1 % 2 != 0:
            print(number1,'é impar')
        elif number1 == 0:
            print(number1,'é neutro')
        else:
            print(number1,'é par')
        

        if number2 % 2 != 0:
            print(number2,'é impar')
        elif number2 == 0:
            print(number2,'é neutro')
        else:
            print(number2,'é par')

    if opcao == 2:
              
        print()
        number1=int(input('digite um numero A: '))
        number2=int(input('digite um numero B: '))   
        print()

        if number1 > 0:
            print(number1, 'é positivo')
        elif number1 == 0:
            print(number1,'é neutro')
        else:
            print(number1, 'é negativo')
                
        if number2 > 0:
            print(number2, 'é positivo')
        elif number2 == 0:
            print(number2,'é neutro')
        else:
            print(number2, 'é negativo')
            
    if opcao == 3:

        print()
        numero1 = input('Digite um número A: ')
        numero2 = input('Digite um número B: ')
        print()

        if '.' in numero1:
            floatNumber = float(numero1)
            print(numero1, 'é decimal')
        elif numero1 == '0':
            print(numero1, 'é neutro')
        else:
            numero1 = int(numero1)
            print(numero1, 'é inteiro')

        if '.' in numero2:
            floatNumber = float(numero2)
            print(numero2, 'é decimal')
            print()
        elif numero2 == '0':
            print(numero2, 'é neutro')
        else:
            numero2 = int(numero2)
            print(numero2, 'é inteiro')
            print()

    
    if opcao == 4:
        print()
        print('é o jao')
        print()
            