import jogo_da_adivinhacao
import jogo_da_forca
import pedra_papel_tesoura


def jogos():
    print("-" * 50)
    print("Bem vindo ao painel de jogos!!")
    print("-" * 50)
    print("Escolha um jogo abaixo:\n"
          "[1] para jogar o jogo da adivinhação\n"
          "[2] para jogar o jogo da forca\n"
          "[3] para jogar o jogo pedra, papel e tesoura\n")

    jogo = int(input("Sua escolha: "))

    if jogo == 1:
        jogo_da_adivinhacao.jogar()
    elif jogo == 2:
        jogo_da_forca.jogar()
    elif jogo == 3:
        pedra_papel_tesoura.jogar()


if __name__ == "__main__":
    jogos()
