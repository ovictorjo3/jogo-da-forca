import jogo as j
import fileHandler as fH

def mostrar_menu():
    print("="*30)
    print(" "*7 + "Jogo da Forca")
    print("="*30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR\n")
    print(""*30)

arquivo = 'score.txt'

if fH.existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo não existe')
    fH.criaArquivo(arquivo)

while True:

    mostrar_menu()

    opcao = int(input("Escolha a opção (1/2/3): "))

    if opcao == 1:
        print( 'Iniciar Jogo!')
        j.Jogar()

    elif opcao == 2:
        print('SCORE')
    elif opcao == 3:
        print('Saindo do jogo... Até mais!')
        break
    else:
        print('Opção inválida... Tente outra.')

