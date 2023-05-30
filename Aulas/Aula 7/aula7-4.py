'''
Em um FOR é possível (mas não muito comum) termos um
ELSE, como exemplificado na imagem a seguir. Quando
terminarmos o FOR das linhas 2 a 5, o ELSE da linha 6 (e
consequentemente a linha 7) serão executados.
• Ao término da execução da linha 7, a linha 8 é executada.

'''

frutas=['maçã','banana','abacaxi']

for fruta in frutas:
    print(fruta)
    print('mais uma linha dentro do for')
    print() #pula linha
else:
    print('else do for')

print('fim do for')
await