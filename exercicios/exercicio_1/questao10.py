#10 Faça um programa que pede dois inteiro e armazene em duas variáveis. 
#Em seguida, troque o valor das variáveis e exiba na tela

number1=int(input('DIGITE SEU PRIMEIRO NUMERO AQUI: '))
number2=int(input('DIGITE SEU SEGUNDO NUMERO AQUI: '))

temp=number1
number1=number2
number2=temp

print("Após a troca, o valor do primeiro numero agora é:",number1)
print("Após a troca, o valor do segundo numero agora é:",number2)
