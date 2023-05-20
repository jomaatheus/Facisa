#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato.

produto1= float(input('digite o preço do primeiro produto: '))

produto2= float(input('digite o preço do segundo produto: '))

produto3= float(input('digite o preço do terceiro produto: '))

menorPreco=produto1
numeroProduto = 1

if produto2 < menorPreco:
    menorPreco = produto2
    numeroProduto = 2


if produto3 < menorPreco:
    menorPreco = produto3
    numeroProduto = 3

print('Você deve comprar o produto', numeroProduto, 'porque é o mais barato.')

#if é uma condição para o produto e o if sera verificado individualmente