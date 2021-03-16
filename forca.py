import random

def boas_vindas():
    print(26 * "*")
    print('Bem Vindo ao Jogo da Forca')
    print(26 * "*")

def carrega_palavra():
    # utilizando o with, não é mais necessário fechar o arquivo aberto .close
    with open("palavras") as arquivo:
        palavras = []

        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicia_letras_acertadas(palavras):
    return ["_" for letra in palavras]

def pede_chute():
    chute = input("Qual a letra?")
    chute = chute.strip().upper()
    return chute

def insere_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_msg_ganhador():
    print("!!!!! GANHOU !!!!!")


def imprime_msg_derrota():
    print("!!!!! GAME-OVER !!!!!")


def jogar():
    boas_vindas()
    palavra_secreta = carrega_palavra()
    letras_acertadas = inicia_letras_acertadas(palavra_secreta)

    tentativas = 0

    enforcou = False
    acertou = False
    print(letras_acertadas)
    #enquanto (true e true)
    while(not enforcou and not acertou):

        chute = pede_chute()


        if(chute in palavra_secreta):
            insere_chute_correto(chute, palavra_secreta, letras_acertadas)

        else:
            tentativas += 1
            print(f'Você errou, faltam {6-tentativas} tentantivas')

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
       imprime_msg_ganhador()
    else:
        imprime_msg_derrota()

if(__name__ == "__main__"):
    jogar()