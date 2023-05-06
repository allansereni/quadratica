class Grupo:

    def __init__(self):
        self.__nome_do_grupo = []
        self.__modalidade = []
        self.__mensalidade_quadra = []
        self.__mensalidade_atleta = []
        self.__avulso_atleta = []

    def get_nome_do_grupo(self, index):
        return self.__nome_do_grupo[index]

    def get_modalidade(self, index):
        return self.__modalidade[index]

    def get_mensalidade_quadra(self, index):
        return self.__mensalidade_quadra[index]

    def get_mensalidade_atleta(self, index):
        return self.__mensalidade_atleta[index]

    def get_avulso_atleta(self, index):
        return self.__avulso_atleta[index]

    def cadastra_grupo(self):
        print("Cadastrar grupo")
        self.__nome_do_grupo.append(input("Qual o nome do grupo? \nNome do grupo:"))
        self.__modalidade.append(input('Modalidade:'))
        self.__mensalidade_quadra.append(eval(input('Valor da mensalidade da quadra:')))
        self.__mensalidade_atleta.append(eval(input('Valor da mensalidade do atleta')))
        self.__avulso_atleta.append(eval(input('Valor avulso do atleta:')))

    def listar_grupo(self, index):
        print('Grupo: {}\nModalidade: {}\nMensalidade da quadra: {}\nMensalidade por atleta: {}\n'
              'Valor avulso por atleta: {}'.format(self.get_nome_do_grupo(index),
                                                   self.get_modalidade(index),
                                                   self.get_mensalidade_atleta(index),
                                                   self.get_mensalidade_atleta(index),
                                                   self.get_avulso_atleta(index)))

    def excluir_grupo(self, index):
        self.__nome_do_grupo.pop(index)
        self.__modalidade.pop(index)
        self.__mensalidade_quadra.pop(index)
        self.__mensalidade_atleta.pop(index)
        self.__avulso_atleta.pop(index)