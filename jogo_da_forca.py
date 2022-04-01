import random


def jogar():

    inicio_do_jogo()

    palavra_secreta = carrega_palavra_secreta()

    print("A palavra secreta é:")
    letras_ocultas = inicializa_palavra_secreta(palavra_secreta)
    print(letras_ocultas)

    enforcou = False
    acertou = False
    erros = 0
    letras_chutadas = []

    while not enforcou and not acertou:

        letra_usuario = chute()

        if letra_usuario in letras_chutadas:
            print("Você já tentou essa letra, tente outra!!!\n")
            print(f'Letras utilizadas: {letras_chutadas}')
            continue

        if letra_usuario in palavra_secreta:
            letras_ocultas = substitui_na_palavra(palavra_secreta, letra_usuario, letras_ocultas)
            letras_chutadas.append(letra_usuario)
        else:
            erros += 1
            erros_possiveis = 6 - erros
            letras_chutadas.append(letra_usuario)
            desenha_forca(erros)
            print(f'Atenção, você pode errar mais {erros_possiveis} vezes\n')

        enforcou = erros == 6
        acertou = '_' not in letras_ocultas

        print(f'\n{letras_ocultas}')

    if acertou:
        mensagem_vencedor()
    if enforcou:
        mensagem_perdedor(palavra_secreta)


def substitui_na_palavra(palavra_secreta, letra_usuario, letras_ocultas):
    indice = 0
    for letra in palavra_secreta:
        if letra == letra_usuario:
            letras_ocultas[indice] = letra

        indice += 1
    return letras_ocultas


def chute():
    chute = input("\nDigite uma letra: ")
    chute = chute.strip().upper()
    return chute


def inicio_do_jogo():
    print("*" * 50)
    print("Bem vindo ao jogo da Forca!!!")
    print("*" * 50)


def inicializa_palavra_secreta(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def carrega_palavra_secreta():
    arquivo = open("Palavras.txt", "r", encoding="utf8")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    indice_da_palavra = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice_da_palavra].upper()
    return palavra_secreta


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      *   ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


def mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    jogar()
