
def jogar():
    print(20*"*")
    print('Bem Vindo no Jogo da Forca')
    print(20*"*")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_",]
    tentativas = 0


    enforcou = False
    acertou = False
    print(letras_acertadas)
    #enquanto (true e true)
    while(not enforcou and not acertou):

        chute = input("Qual a Letra?")
        chute = chute.strip().upper()
        index = 0

        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print(f'Você errou, faltam {6-tentativas} tentantivas')
        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("!!!!!GANHOU!!!!!")
    else:
        print("!!!!!ENFORCADO!!!!!")
    print("!!!!!Fim do Jogo!!!!!")

if(__name__ == "__main__"):
    jogar()