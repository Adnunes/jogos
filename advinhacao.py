import random

def jogar():
    print(20*"*")
    print('Jogo de Adivinhação')
    print(20*"*")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 3
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print("(1) fácil, (2) médio, (3) Difícil")

    nivel = int(input("Definir o nível: "))

    if (nivel == 1 ):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):

        print("tentativas: {} de {} ".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = (numero_secreto == chute)
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Você digitou: ", chute)

        if (acertou):
            print('Você acertou e fez {}'.format(pontos))
            break

        else:
            if(maior):
                print("Você errou !! o seu chute foi maior do que o numero secreto")

            elif(menor):
                print("Você errou !! o seu chute foi menor do que o numero secreto")

            pontos_perdidos = abs(numero_secreto - chute) #40 - 20 = 20
            pontos = pontos - pontos_perdidos

       # rodada = rodada + 1 no for não é preciso incrementar, ele ja faz isso

    print("!!!!!Fim do Jogo!!!!!")

if(__name__ == "__main__"):
    jogar()