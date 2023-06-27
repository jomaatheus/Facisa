from operacoesbd import *

def listar_reclamacoes(conexao):
    consultaTipo = 'SELECT codigo, titulo, descricao, autor, tipo, datahora FROM manifestacao'
    listaReclamacoes = listarBancoDados(conexao, consultaTipo)

    if len(listaReclamacoes) == 0:
        print('Lista vazia!')
    else:
        for elemento in listaReclamacoes:
            print('Código:', elemento[0], 'Título:', elemento[1], 'Descrição:', elemento[2], 'Autor:', elemento[3], 'Tipo:', elemento[4], 'Data:', elemento[5])
            print()

def listar_por_tipo(conexao):
    tipo = int(input('1 - Reclamação 2 - Sugestão 3 - Elogio: '))

    if tipo in [1, 2, 3]:
        sqlTipo = 'SELECT codigo, titulo, descricao, autor, tipo, datahora FROM manifestacao WHERE tipo = %s'
        valores = [tipo]
        listaReclamacoes = listarBancoDados(conexao, sqlTipo, valores)

        if len(listaReclamacoes) == 0:
            print()
            print('Lista vazia!')
        else:
            for elemento in listaReclamacoes:
                print('Código:', elemento[0], 'Título:', elemento[1], 'Descrição:', elemento[2], 'Autor:', elemento[3], 'Tipo:', elemento[4],'Data:', elemento[5])
                print()
    else:
        print('Opção inválida!')

def criar_manifestacao(conexao):
    titulo = input('Digite a manifestação: ')
    descricao = input('Digite uma descrição: ')
    autor = input('Digite seu nome: ')
    tipo = int(input('1 - Reclamação 2 - Sugestão 3 - Elogio: '))
    print()

    sqlInsercao = 'INSERT INTO manifestacao (titulo, descricao, autor, tipo, datahora) VALUES (%s, %s, %s, %s, NOW())'
    valores = [titulo, descricao, autor, tipo]
    insertNoBancoDados(conexao, sqlInsercao, valores)
    print("Adicionado com sucesso!")

def exibir_manifestacoes(conexao):
    consultarQuantidadeReclamacoes = 'SELECT COUNT(*) FROM manifestacao WHERE tipo = 1'
    consultarQuantidadeSugestoes = 'SELECT COUNT(*) FROM manifestacao WHERE tipo = 2'
    consultarQuantidadeElogios = 'SELECT COUNT(*) FROM manifestacao WHERE tipo = 3'

    resultadoReclamacoes = listarBancoDados(conexao, consultarQuantidadeReclamacoes)
    resultadoSugestoes = listarBancoDados(conexao, consultarQuantidadeSugestoes)
    resultadoElogios = listarBancoDados(conexao, consultarQuantidadeElogios)

    quantidadeReclamacoes = resultadoReclamacoes[0][0]
    quantidadeSugestoes = resultadoSugestoes[0][0]
    quantidadeElogios = resultadoElogios[0][0]

    print('Quantidade de reclamações:', quantidadeReclamacoes)
    print('Quantidade de sugestões:', quantidadeSugestoes)
    print('Quantidade de elogios:', quantidadeElogios)

def pesquisar_por_codigo(conexao):
    codigo = input('Digite o código da manifestação: ')
    consultaListagem = 'SELECT codigo, titulo, descricao, autor, tipo, datahora FROM manifestacao WHERE codigo = ' + codigo

    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        print()
        print('Nenhuma manifestação encontrada com o código fornecido.')
    else:
        for elemento in listaReclamacoes:
            print('Código:', elemento[0], 'Título:', elemento[1], 'Descrição:', elemento[2], 'Autor:', elemento[3], 'Tipo:', elemento[4],'Data:', elemento[5])
            print()

def alterar_titulo_e_descricao(conexao):
    codigo = input('Digite o código da manifestação: ')
    consultaListagem = 'SELECT codigo FROM manifestacao WHERE codigo = %s'
    dados = [codigo]
    resultado = listarBancoDados(conexao, consultaListagem, dados)

    if len(resultado) == 0:
        print()
        print('Nenhuma manifestação encontrada com o código fornecido.')
    else:
        novoTitulo = input('Digite o novo título da manifestação: ')
        novaDescricao = input('Digite a nova descrição da manifestação: ')

        sqlAtualizar = 'UPDATE manifestacao SET titulo = %s, descricao = %s WHERE codigo = %s'
        valores = [novoTitulo, novaDescricao, codigo]

        linhasAfetadas = atualizarBancoDados(conexao, sqlAtualizar, valores)

        if linhasAfetadas > 0:
            print('Atualizado com sucesso!')
        else:
            print('Ocorreu um erro ao atualizar a manifestação.')


def excluir_manifestacao(conexao):
    codigo = input('Digite o código da manifestação: ')
    consultaListagem = 'DELETE FROM manifestacao WHERE codigo = %s'
    dados = [codigo]
    linhasAfetadas = excluirBancoDados(conexao, consultaListagem, dados)

    if linhasAfetadas > 0:
        print()
        print('Manifestação excluída com sucesso!')
    else:
        print()
        print('Nenhuma manifestação encontrada com o código fornecido.')
