#v1 Marromenos
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F -Feminino, M -Masculino, Sexo Inválido.

sexo = input('Digite o sexo M ou F: ')

if sexo == 'M' or sexo == 'm':
    print('Masculino')
elif sexo == 'F' or sexo == 'f':
    print('Feminino')
else:
    print('Caio')
    
#v2 Marromenos

sexo = input('Digite o sexo M ou F: ')
sexo = sexo.lower()

if sexo == 'm':
    print('Masculino')
elif sexo == 'f':
    print('Feminino')
else:
    print('Caio')
    
#v3 sonho de consumo

sexo = input('Digite o sexo M ou F: ')

if sexo in 'mM':
    print('Masculino')
elif sexo in 'fF':
    print('Feminino')
    
    
# exemplo criado por Caio (aluno da noite)

palavrao = input('Digite o palavrao: ')

if palavrao in 'porracaralhomizerafoda':
    print('Modere a boca, abestado!')
else:
    print('boca limpa :D')