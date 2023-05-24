'''
Existe 3 opções (“sabores”) para a função
range:
• range(n)na qual gera números de 0 até n-1
• Por exemplo, range(3) gera 0,1 e 2
• range(a,n)na qual gera números de a até n-1
• Por exemplo, range(1,3) gera 1 e 2
• range(a,n,s) na qual gera números de a até n-1,
pulando de s em s

Por exemplo, range(0,5,2) em teoria geraria
0,1,2,3,4 . Entretanto, o último parâmetro
(s) que tem o valor 2 significa que ele pula
de 2 em 2. Como assim? No 0, ele pula
diretamente para 2 e do 2 exatamente para
o 4, de modo que os 1 e 3 são
desconsiderados.
'''

print(range(5))
print(list(range(5)))
print(list(range(0,5)))
print(list(range(0,5,2)))