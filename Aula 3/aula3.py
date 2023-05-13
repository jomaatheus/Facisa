'''
• Uma estrutura muito importante na programação são os
condicionais e, neste momento, nos aprofundaremos sobre o
comando IF.
• Para entendermos melhor o IF, tomemos como exemplo o
código a seguir
'''
idade= 67

if idade >= 65:
    print('acesso gratuito ao ônibus')
print('fim do programa')

'''
• No código acima,temos os seguintes destaques:
• Na linha 3, temos o nosso condicional IF
• A condição é se aidade é maior ou igual a 65
• Ao término da condição,temos um dois pontos (:)
• A linha 4, verificamos um recuo (espaço), que indica
que,esta linha, “pertence” ao IF da linha 3,de modo
que, esta linha 4 só será exibida se o IF da linha 3 for
verdadeiro (neste exemplo é verdadeiro)
• A linha 5, como pode-se perceber, não tem espaço,
de modo que éexecutada independente do resultado
(verdadeiro ou falso) do IF.
• Para alinhar o entendimento, apresentamos novamente a
imagem a seguir. Se a expressão do IF for verdadeira, as linhas
de código 1, 2 e 3 são executadas. Enquanto que, a linha
“outra linha qualquer” é apresentada sempre.
'''