#• Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F -Feminino, M -Masculino, Sexo Inválido

sexualidade=input('digite sua sexualidade (F -Feminino, M -Masculino):')

if sexualidade == "F" or sexualidade== "f":
    print('Feminino')

elif sexualidade == "M" or sexualidade =="m":
    print('Masculino')

else:
    print('Sexo invalido')


