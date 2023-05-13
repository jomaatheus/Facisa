#7 Realiza a leitura de 1 int e apresenta se ele é par ou ímpar.
number=int(input('Digite seu numero aqui: '))
resto= number % 2

if resto == 0:
    print('Seu numero é par')
else:
    print('Seu numero é impar')