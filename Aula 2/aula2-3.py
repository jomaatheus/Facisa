'''
Para armazenar caracteres (que ainda assim, podem ser
números), usamos o tipo str(String). No exemplo a seguir,
apresentamos um exemplo do uso de Strings.
• Para declarar Strings, basta atribuir um valor entre
aspas simples ou duplas a uma variável
• Nas linhas 1 a 3, declaramos 3 variáveis. Verifique que, a
variável idade, tende a ser int, mas ainda assim, podemos
declarar como string, pois a colocamos entre aspas
• Nas linhas seguintes, apenas apresentamos os textos
concatenados

'''

nome='João'
sobrenome='Matheus'
idade='19'

print(nome + sobrenome)
print('João'+'Matheus')
print('Possui a idade',idade)

'''
Para finalizar, no exemplo a seguir apresentamos o uso do método
len, que se refere a lenght, que é o tamanho da String. Note que,
imprimimos o tamanho de duas maneiras o tamanho da String
‘João’, que possui 6 caracteres.
• Na primeira (linha 2), chamamos diretamente o método
lendurante o print
• A segunda abordagem (linhas 4 e 5), atribui o tamanho da
String a uma variável antes de entrar no print.

'''

nome='João'
print('O tamanho do nome tem',len(nome),'caracteres')

tamanhoTexto= len(nome)
print('O tamanho do nome tem',tamanhoTexto,'caracteres')