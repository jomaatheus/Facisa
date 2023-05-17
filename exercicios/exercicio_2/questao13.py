#• Tendo como dado de entrada a altura (h) de uma pessoa, 
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#• Para homens: (72.7*h) –58
#• Para mulheres: (62.1*h) -44.7

altura=float(input('digite sua altura: '))

h=altura

genero = input("Digite o gênero da pessoa (M para masculino ou F para feminino): ")

homens= (72.7*h) - 58
homens=round(homens,2)

mulheres= (62.1*h) - 44.7
mulheres=round(mulheres,2)


if genero == 'M' or genero == 'm':
    peso_ideal = round(homens, 2)
    print("O peso ideal para um homem com essa altura é:", peso_ideal, "kg")
elif genero == 'F' or genero == 'f':
    peso_ideal = round((62.1 * altura) - 44.7, 2)
    print("O peso ideal para uma mulher com essa altura é:", mulheres, "kg")
else:
    print("Gênero inválido. Por favor, digite M para masculino ou F para feminino.")





