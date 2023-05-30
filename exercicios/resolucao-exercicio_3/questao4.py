#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

caractere = input('Digite o caractere: ')
caractere = caractere.lower()

if caractere in 'aeiou':
    print('Vogal')
elif caractere in 'bcdfghjklmnpqrstvwxyz':
    print('Consoante')
else:
    print('caio! caractere especial')
    