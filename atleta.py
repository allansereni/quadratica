from grupo import Grupo

class Atleta:

    def __init__(self):
        self.__nome = []
        self.__idade = []
        self.__telefone = []
        self.__posicao = []
        self.__estrela = []
        self.__admin = []
        self.__frequencia = []
        self.__valor_pagar = []

    def set_nome(self, nome):
        self.__nome.append(nome)

    def get_nome(self, index):
        return self.__nome[index]

    def set_idade(self, idade):
        self.__idade.append(idade)

    def get_idade(self, index):
        return self.__idade[index]

    def set_telefone(self, telefone):
        self.__telefone.append(telefone)

    def get_telefone(self, index):
        return self.__telefone[index]

    def set_posicao(self, posicao):
        self.__posicao.append(posicao)

    def get_posicao(self, index):
        return self.__posicao[index]

    def set_estrela(self, estrela):
        self.__estrela.append(estrela)

    def get_estrela(self,index):
        return self.__estrela[index]

    def set_frequencia(self, frequencia):
        self.__frequencia.append(frequencia)

    def get_frequencia(self, index):
        return self.__frequencia[index]

    def set_admin(self, admin):
        self.__admin.append(admin)

    def get_admin(self, index):
        return self.__admin[index]

    def set_valor_pagar(self, valor_pagar):
        self.__valor_pagar.append(valor_pagar)

    def get_valor_pagar(self, index):
        return self.__valor_pagar[index]

    def cadastrar_atleta(self):
        print("Cadastrar atleta")
        self.__nome.append(input("Nome:"))
        self.__idade.append(int(input('Idade:')))
        self.__telefone.append(input('Telefone:'))
        self.__posicao.append(input('Posição:'))
        self.__estrela.append(int(input('Estrelas:')))
        self.__admin.append(input('Administrador? (s)sim / (n)não :'))
        self.__frequencia.append(input('Mensal ou avulso:'))
        #if (frequencia.upper() == 'MENSAL'):
        #    valor_pagar = mensalidade_atleta
        #else:
        #    valor_pagar = avulso_atleta

    def listar_atleta(self, index):
        print('Nome do atleta: {}\nIdade: {}\nTelefone{}\nPosição: {}\nEstrelas: {}\nFrequência: {}'
              .format(self.get_nome(index), self.get_idade(index), self.get_telefone(index),
                      self.get_posicao(index), self.get_estrela(index), self.get_frequencia(index)))

    def excluir_atleta(self, index):
        self.__nome.pop(index)
        self.__idade.pop(index)
        self.__telefone.pop(index)
        self.__posicao.pop(index)
        self.__estrela.pop(index)
        self.__admin.pop(index)
        self.__frequencia.pop(index)
       # self.__valor_pagar.pop(index)