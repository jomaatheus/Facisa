'''
O uso de operadores matemáticos com Strings é funcional
• O operador soma, funciona para juntar 2 Strings (concatenar)
• Os operadores subtração e divisão não possuem
funcionamento com Strings
• Como vou fazer ‘joao’/2? `Daniel`-2?
• O operador multiplicação possui uso no Python
• `Daniel`*3 exibe DanielDanielDaniel
• O exemplo a seguir demonstra o funcionamento do que
acabamos de discutir. As linhas 1,2,3 e 6 funcionam, enquanto
todas as outras apresentam erro.

'''

nome="João"
sobrenome='Matheus'
print(nome + sobrenome)
#print(nome + 3) não funciona
#print(nome - 3) não funciona
print(nome * 3)
#print(nome / 3) não funciona