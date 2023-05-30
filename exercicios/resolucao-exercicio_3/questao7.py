#menor preco

preco1 = float(input('digite o preco '))
preco2 = float(input('digite o preco '))
preco3 = float(input('digite o preco '))

precos = [ ]
precos.append(preco1)
precos.append(preco2)
precos.append(preco3)

menor = min(precos)
print('menor eh',menor)