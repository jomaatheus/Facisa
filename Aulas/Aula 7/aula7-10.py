'''
Exemplo #2: Este se refere a um dos usos comuns do WHILE,
que é de apresentar menus de opções ao usuário. No exemplo a
seguir, ele vai apresentar as opções 1) Saque 2) Extrato 3) Sair
enquanto o usuário não digitar 3, que é Sair da aplicação.

'''

print('Bem-vindo ao banco')

command='0'
while command != '3':
    print('1) Saque 2) Extrato 3) Sair')
    command=input('digite sua opção: ')
    #funcionamento do programa