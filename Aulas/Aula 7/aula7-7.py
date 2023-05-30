'''
Exemplo #3: Com o continue podemos parar a iteração atual do
loop e continuar com a próxima. No exemplo a seguir, quando ele
encontrar banana (linha 3), vai pular para o próximo elemento.

'''

frutas=['maçã','banana','abacaxi']

for fruta in frutas:
    if fruta == 'banana ':
        continue
    print('a fruta é', fruta)
    print('mais uma linha dentro do for')
    print() # pular linha