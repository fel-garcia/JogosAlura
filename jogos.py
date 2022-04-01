import jogo_da_adivinhacao
import jogo_da_forca


def jogos():
    print("-" * 50)
    print("Bem vindo ao painel de jogos!!")
    print("-" * 50)
    print("Escolha um jogo abaixo:\n"
          "[1] para jogar o jogo da adivinhação\n"
          "[2] para jogar o jogo da forca\n")

    jogo = int(input("Sua escolha: "))

    if jogo == 1:
        jogo_da_adivinhacao.jogar()
    elif jogo == 2:
        jogo_da_forca.jogar()


if __name__ == "__main__":
    jogos()
