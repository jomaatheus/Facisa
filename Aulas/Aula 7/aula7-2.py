'''
• O operador FOR é usado para iterar sobre uma sequência (lista,
dupla, String), entre outros objetos iteráveis. O formato é o
seguinte.

'''

frutas=['maçã','uva','banana']

for fruta in frutas:
    print(fruta)
    print('mais uma linha dentro do FOR')
    print() #pula linha

print('bye FOR')



'''
Acima temos um exemplo comum do uso do FOR. Na linha 1,
declaramos uma lista de frutas, contendo 3 frutas. Na linha 2,
usamos o FOR, onde fruta é uma variável temporária, que guarda o
valor de cada fruta da lista.Como temos 3 itens na lista frutas,o for
executará 3 vezes,de modo que as linhas 3,4 e 5 serão executadas 3 
vezes.
• Na primeira iteração, a linha 3 imprimirá maça, depois
imprime a linha 4 e pula a linha(linha5)
• Na segunda iteração, a linha 3 imprimirá banana, depois
imprime alinha 4 e pula a linha(linha5)
• a linha 3 imprimirá abaxai, depois imprime a linha 4 e pula
a inha(linha5)

'''