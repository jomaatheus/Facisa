#• Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Digite a data no formato dd/mm/aaaa: ')

# Verifica se a data possui 10 caracteres (dd/mm/aaaa) e se o caractere '/' está nas posições corretas
if len(data) == 10 and data[2] == '/' and data[5] == '/':
    dia = int(data[:2])  # Extrai o dia da string e converte para inteiro
    mes = int(data[3:5])  # Extrai o mês da string e converte para inteiro
    ano = int(data[6:])  # Extrai o ano da string e converte para inteiro

    # Verifica se o ano é bissexto
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    # Verifica se a data é válida
    data_valida = (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12)

    # Verifica se o dia é válido para o mês específico
    if mes in [4, 6, 9, 11]:
        data_valida = data_valida and (dia <= 30)
    elif mes == 2:
        if bissexto:
            data_valida = data_valida and (dia <= 29)
        else:
            data_valida = data_valida and (dia <= 28)

    # Imprime o resultado
    if data_valida:
        print('A data é válida.')
    else:
        print('A data é inválida.')
else:
    print('Formato de data inválido. Utilize o formato dd/mm/aaaa.')
