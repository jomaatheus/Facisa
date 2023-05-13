'''
• Na seção anterior, usamos o operador de comparação >= para
verificar se a idade é maior ou igual a 65,lembram? Na sequencia
temos a lista dos principais operadores de comparação existentes
no Python.
Operador Operação               Exemplo
==       Igualdade           If idade == 18:
!=       Diferente           If idade != 18:
>        Maior que           If idade > 18:
<        Menor que           If idade < 18:
>=       Maior ou igual que  If idade >= 18:
<=       Menor ou igual que  If idade <= 18:

• Para consolidar o que foi apresentado anteriormente, no
programa a seguir, relacionamos o uso de todos os operadores de
comparação:


'''

idade=67

if idade == 18:
    print('você tem 18 anos')

if idade != 18:
    print('você não tem 18 anos')

if idade > 18:
    print('você tem mais de 18 anos')

if idade < 18:
    print('você tem menos de 18 anos')

if idade >= 18:
    print('você tem 18 anos ou mais')

if idade <= 18:
    print('você tem 18 anos ou menos')
