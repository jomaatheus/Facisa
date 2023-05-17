#• Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#• o produto do dobro do primeiro com metade do segundo .
#• a soma do triplo do primeiro com o terceiro.
#• o terceiro elevado ao cubo

number1=int(input("digite o seu primeiro numero inteiro: "))
number2=int(input("digite o seu segundo numero inteiro: "))
number3=float(input("digite o seu numero real: "))

produto=(2*number1)*(number2/2)

soma=(3*number1)+ number3

cubo=number3**3

print("O produto do dobro do primeiro com metade do segundo é:", produto)
print("A soma do triplo do primeiro com o terceiro é:", soma)
print("O terceiro elevado ao cubo é:", cubo)