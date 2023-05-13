'''
 Comumente calculamos o Índice de Massa Corpórea
(IMC)para verificar se estamos no peso ideal .A fórmula
é a seguinte:
IMC= peso/altura²
'''

peso=float(input('digite seu peso aqui: '))

altura=float(input('digite sua altura aqui: '))

imc=peso/altura**2

if imc < 16:
    print('Magreza Grave')

elif imc >= 16 and imc <17:
    print('Magreza Moderada')

elif imc >=17 and imc < 18.5:
    print('Magreza leve')

elif imc >= 18.5 and imc <25:
    print('Saúdavel')

elif imc >= 25 and imc <30:
    print('Sobrepeso')

elif imc >= 30 and imc <35:
    print('Obesidade Grau 1')

elif imc >= 35 and imc <40:
    print('Obesidade Grau 2(severa)')

else:
    print('Obesidade Grau 3(morbida)')