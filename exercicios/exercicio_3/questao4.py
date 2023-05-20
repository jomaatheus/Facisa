#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra=input('digite uma letra: ')

vogais=['a','e','i','o','u']
if letra.lower() in vogais:
    print('vogais')
else:
    print('consoante')