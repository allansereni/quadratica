def criar_grupo():
    print('Criar grupo')
    global nome_grupo
    global modalidade
    global mensalidade_quadra
    global mensalidade_atleta
    global avulso_atleta
    nome_grupo = input("Qual o nome do grupo? \nNome do grupo:")
    modalidade = input('Modalidade:')
    mensalidade_quadra = eval(input('Valor da mensalidade da quadra:'))
    mensalidade_atleta = eval(input(('Valor da mensalidade do atleta')))
    avulso_atleta = eval(input('Valor avulso do atleta:'))

def cadastrar_atleta():
    print("Dados do atleta")
    global nome_atleta
    global idade_atleta
    global posicao_atleta
    global estrelas_atleta
    global admin
    global frequencia_atleta
    global valor_a_pagar
    nome_atleta = input('Nome:')
    idade_atleta = int(input('Idade:'))
    posicao_atleta = input('Posição:')
    estrelas_atleta = int(input('Estrelas:'))
    admin = input('Administrador? (s)sim / (n)não :')
    frequencia_atleta = input('Mensal ou avulso:')
    valor_a_pagar = 0
    if (frequencia_atleta.upper() == 'MENSAL'):
        valor_a_pagar = mensalidade_atleta
    else:
        valor_a_pagar = avulso_atleta

sair = 0


while (sair == 0):
    print('************************************************')
    print('****   Quadrática - Administre sua quadra   ****')
    print('************************************************')

    print('Menu')
    print('1 - Criar grupo')
    print('2 - Cadastrar atleta')
    print('3 - Listar grupos')
    print('4 - Listar ateltas')
    print('5 - excluir atleta')
    print('6 - Excluir grupo')
    print('7 - Sair')

    opcao = eval(input('Selecione a opção:'))
    if (opcao < 1 or opcao > 7):
        print('Opção inválida! Escolha uma opção válida!')
        continue
    elif (opcao == 1):

        criar_grupo()

    elif (opcao == 2):

        cadastrar_atleta()

    elif (opcao == 3):
        print('Grupo: {}\nModalidade: {}\nMensalidade da quadra: {}\nMensalidade por atleta: {}\n'
              'Valor avulso por atleta: {}'.format(nome_grupo, modalidade, mensalidade_quadra,
                                                   mensalidade_atleta, avulso_atleta))
    elif (opcao == 4):
        print('Grupo: {}\nModalidade: {}\nNome do atleta: {}\nIdade: {}\n''Posição: {}\nEstrelas: {}'
              '\nFrequência: {}\nValor a pagar: R${}'.format(nome_grupo, modalidade, nome_atleta,
                                                             idade_atleta, posicao_atleta, estrelas_atleta,
                                                             frequencia_atleta, valor_a_pagar))
    elif (opcao == 5):
        print('Atleta excluído!')
    elif (opcao == 6):
        print('Grupo excluído!')
    elif (opcao == 7):
        sair = 1
