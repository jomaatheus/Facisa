'''
• Faça um programa que leia e valide as seguintes informações:
• Nome: maior que 3 caracteres;
• Idade: entre 0 e 150;
• Salário: maior que zero;
• Sexo: 'f' ou 'm';
• Estado Civil: 's', 'c', 'v', 'd’;

'''


nome=input('digite seu nome: ')
while len(nome) <= 3:
        print('digite um nome maior que 3 caracteres!')
        nome=input('digite seu nome: ')


idade=int(input('digite sua idade: '))
while idade < 0 or idade > 150:
    print('digite sua idade novamente')
    idade=int(input('digite sua idade: '))


salario=int(input('digite seu salario: '))
while salario <= 0:
    print('digite um salario maior que zero')
    salario=int(input('digite seu salario: '))


sexo=input('digite seu sexo(f/m): ')
while sexo.lower() != 'f' and sexo.lower() != 'm':
        print('digite um sexo valido.')
        sexo=input('digite seu sexo(f/m): ')

estadoCivil=input('Digite seu estado civil (s/c/v/d): ')
while estadoCivil.lower() != 's' and estadoCivil.lower() !='c' and estadoCivil.lower() != 'v' and estadoCivil.lower() != "d":
    print('digite um estado civil valido.')
    estadoCivil=input('Digite seu estado civil (s/c/v/d): ')

print('Informações válidas:')
print('Nome:', nome)
print('Idade:', idade)
print('Salário:', salario)
print('Sexo:', sexo)
print('Estado Civil:', estadoCivil)