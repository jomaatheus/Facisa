'''
** - Potência - 2 ** 3 = 8
% - Módulo - 5 % 2 = 1
// - Divisão inteira - 22 // 8 = 2
* - Multiplicação - 3 * 8 = 24
- - Subtração - 8 – 2 = 6
+ - Soma - 2 + 2 = 4
/ - Divisão - 33 / 4 = 8.25

'''
#O operador +, que se refere obviamente a soma, pode ser
# utilizado em números (inte float), bem como em strings (str).

nome= 'joao'
sobrenome='matheus'
nomeCompleto= nome + sobrenome
print('o meu nome completo é', nomeCompleto)

'''
• No exemplo acima, criamos duas variáveis (nome e sobrenome) e,
uma terceira variável que é a junção das duas anteriores. A esta
operação de junção, comumente chamamos de concatenação.
• A concatenação deve sempre ser entre str(Strings) e inteiros, 
sem poder misturar. Ou seja, o exemplo a seguir (misturando str e int) não funciona em Python
'''