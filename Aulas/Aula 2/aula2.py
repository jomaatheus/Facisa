'''
• Usamos a função print para apresentação dos dados
• No exemplo abaixo:
• Na linha 1, a variável saldo recebe um valor com 5
casas decimais
• Na linha 2, exibimos o saldo com as 5 casas decimais
• Na linha 3, imprimimos uma linha em vazio
• Por fim, na linha 4, exibimos o mesmo saldo (da linha
2), mas com apenas 2 casas decimais
• Verifique que, na parte %.2f, o f se refere a
float, enquanto que o número 2, se refere a
quantidade de casas decimais
• Se fosse int, seria d (ao invés de f)

'''

saldo= 1000.50123
print('o saldo é',saldo)
print()
print("o saldo é %.2f" %saldo) 