import random


def jogar():
    print("*" * 50)
    print("Bem vindo ao jogo da Advinhação!!!")
    print("*" * 50)

    numero_secreto = random.randrange(1, 101)

    print("Escolha a dificuldade do Jogo:\n[1] Fácil.\n[2] Médio.\n[3] Difícil.\n")
    dificuldade = int(input("Escolha: "))

    if dificuldade == 1:
        tentativas = 10
    elif dificuldade == 2:
        tentativas = 5
    elif dificuldade == 3:
        tentativas = 3
    else:
        print('Por favor, escolha um número de 1 a 3!!\n')
        jogar()

    for rodada in range(1, tentativas + 1):
        print(f'Rodada {rodada} de {tentativas}')
        print("*" * 50)
        numero_usuario = int(input("Digite um número entre 1 e 100 "))
        pontos = abs(numero_secreto - numero_usuario)

        limite_maior = numero_usuario > 100
        limite_menor = numero_usuario < 1

        if limite_menor or limite_maior:
            print("Por favor, digite um número entre 1 e 100\n")
            continue

        acertou = numero_usuario == numero_secreto
        chute_menor = numero_usuario < numero_secreto
        chute_maior = numero_usuario > numero_secreto

        if acertou:
            print("Parabéns, você acertou o número secreto!!!!")
            break
        elif chute_maior:
            print("Você errou!! Seu chute foi maior que o número secreto\n")
        else:
            print("Você errou!! Seu chute foi menor que o número secreto\n")

    if chute_maior or chute_menor:
        print(f'Você errou por {pontos}')


if __name__ == "__main__":
    jogar()
