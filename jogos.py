import forca
import advinhacao

def escolhe_jogo():
    print(20*"*")
    print('Escolha o seu Jogo')
    print(20*"*")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual o jogo?"))

    if (jogo==1):
        print("jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("jogando adivinhação")
        JogoAdvinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()