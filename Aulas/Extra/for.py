feira=['uva','caju','kiwi']

for item in feira:
    print(item)
#item é uma variavel temporaria, poderia ser qualquer nome

print('bye')

for i in range(3):
    print(i+1, 'elemento',feira[i])
# vai colocar uma sequencia em cada elemento da lista

'''
for i in range(len(feira)):
    print(i+1, 'elemento',feira[i])

--> vai acompanhar o desenvolvimento da lista, se ela adicionar ou remover um  elemento

'''