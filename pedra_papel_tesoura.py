import random


def jogar():
    print("*" * 50)
    print("Bem vindo ao Pedra, Papel, Tesoura!")
    print("*" * 50)
    denovo = True

    while denovo:
        oponente = random.choice(['Pedra', 'Papel', 'Tesoura'])
        usuario = int(input("[1] Pedra\n"
                            "[2] Papel\n"
                            "[3] Tesoura\n"
                            "Escolha: "))

        escolhas = {1: 'Pedra', 2: 'Papel', 3: "Tesoura"}
        usuario = escolhas[usuario]

        print(f"\nEu escolhoooo......  {oponente}\n")

        win = vitoria(usuario, oponente)
        print(win)

        denovo = novamente()


def vitoria(usuario, oponente):
    # R > T, T > P, P > R

    vitoria1 = usuario == "Pedra" and oponente == "Tesoura"
    vitoria2 = usuario == "Tesoura" and oponente == "Papel"
    vitoria3 = usuario == "Papel" and oponente == "Pedra"

    if vitoria1 or vitoria2 or vitoria3:
        return "Meus grandes parabéns, você venceu!!"
    elif usuario == oponente:
        return "Ah não... Empatou!!"
    else:
        return "HAHA Ganhei de você!!"


def novamente():
    denovo = input("\nJogar novamente?\n[S] Sim\n[N] Não\n--")
    if denovo == "s":
        return True
    else:
        return False


if __name__ == "__main__":
    jogar()
