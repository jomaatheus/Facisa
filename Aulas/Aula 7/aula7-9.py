'''
WHILE(Enquanto,em português )permite que você execute um
bloco de código (corpo) repetidamente enquanto uma condição
for True (verdadeira),conforme exemplo a seguir.

'''
#while condicao
#corpo - linha de codigo 1
#corpo - linha de codigo 2

'''
Exemplo #1: Enquanto o número for menos que 6, vai imprimir
o número (linha 3). Entretanto, na linha 4, incrementamos
(somamos 1) o número de modo que, ele vai imprimir até 5 e
para (critério de parada -fim).

'''

numero=1

while numero <6:
    print(numero)
    numero= numero+1
print ('terminou o loop')