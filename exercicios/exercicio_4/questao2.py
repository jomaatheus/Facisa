'''
• Faça um programa que leia um nome de usuário e a 
sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de
erro e voltando a pedir as informações.

'''
print()
nomeUsuario=input('digite um nome de usuario: ')
nomeUsuario=nomeUsuario.lower()
senha=input('digite uma senha: ')
senha=senha.lower()

while nomeUsuario == senha:
    print()
    print('erro digite as informações novamente')
    print()
    nomeUsuario=input('digite um nome de usuario: ')
    nomeUsuario=nomeUsuario.lower()
    senha=input('digite uma senha: ')
    senha=senha.lower()
    print()
else:
    print('Seja bem-vindo')
    print()