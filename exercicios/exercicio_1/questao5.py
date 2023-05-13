#5 Realiza a leitura de 1 float
#referente ao valor de um produto e imprime o valor com descontos de 10%, 20% e 50%

value=float(input('digite o valor do produto aqui: '))

discount1=value*0.9
discount2=value*0.8
discount3=value*0.5

finalValue=discount1,discount2,discount3

print('O valor do desconto é respectivamente:',finalValue)
