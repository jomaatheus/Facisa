'''
Exemplo #4: Com a instrução break podemos interromper o
loop antes que ele tenha percorrido todos os itens, como no
exemplo a seguir. Exibimos maça e depois banana. Abacaxi
não será exibido.

'''

frutas=['maçã','banana','abacaxi']

for fruta in frutas:
    print('a fruta é', fruta)
    print('mais uma linha dentro do for')
    print() # pular linha
    if fruta == 'banana':
        break
    print('outra linha')