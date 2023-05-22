#Faça um Programa que leia um número inteiro menor que 1000 e 
#imprima a quantidade de centenas, dezenas e unidades do mesmo.
#• Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#• 326 = 3 centenas, 2 dezenas e 6 unidades
#• 12 = 1 dezena e 2 unidades Testar com:
#326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input('Digite um número inteiro menor que 1000: '))

if numero >= 1000:
    print("O número fornecido é maior ou igual a 1000.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    resultado = ""
    if centenas > 0:
        resultado += str(centenas) + " centena(s), "
    if dezenas > 0:
        resultado += str(dezenas) + " dezena(s), "
    if unidades > 0 or numero == 0:
        resultado += str(unidades) + " unidade(s)"

    print(resultado)