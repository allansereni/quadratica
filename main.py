from atleta import Atleta
from grupo import Grupo

def main():
    a = Atleta()
    g = Grupo()

    sair = 0

    while (sair == 0):
        
        menu()
        
        opcao = eval(input('Selecione a opção:'))
        if (opcao < 1 or opcao > 7):
            print('Opção inválida! Escolha uma opção válida!')
            continue
        elif (opcao == 1):

            g.cadastra_grupo()

        elif (opcao == 2):

            a.cadastrar_atleta()

        elif (opcao == 3):

            g.listar_grupo(0)

        elif (opcao == 4):

            a.listar_atleta(0)

        elif (opcao == 5):

            confirma = input("Você tem certeza? (s)sim \ (n)não: ")
            if (confirma.upper() == "S"):
                g.excluir_grupo(0)
            else:
                continue

        elif (opcao == 6):

            confirma = input("Você tem certeza? (s)sim \ (n)não: ")
            if (confirma.upper() == "S"):
                a.excluir_atleta(0)
            else:
                continue

        elif (opcao == 7):
            confirma = input("Você tem certeza? (s)sim \ (n)não: ")
            if (confirma.upper() == "S"):
                sair = 1
            else:
                continue


def menu():
    print('************************************************')
    print('****   Quadrática - Administre sua quadra   ****')
    print('************************************************')

    print('Menu')
    print('1 - Criar grupo')
    print('2 - Cadastrar atleta')
    print('3 - Listar grupos')
    print('4 - Listar ateltas')
    print('5 - Excluir grupo')
    print('6 - Excluir atleta')
    print('7 - Sair')
    

if __name__ == "__main__":
    main()