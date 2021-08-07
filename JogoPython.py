def EscreveCabecalho():
    print("********************")
    print("Jogo de adivinhação.")
    print("********************")


EscreveCabecalho()

total_tentativas = 3
numero = 52

for rodada in range(1, total_tentativas + 1):
    print("Rodada {} de {}".format(rodada, total_tentativas))

    chute = int(input("Digite um número entre 1 e 100: "))
    chute_valido = 0 < chute <= 100
    acertou = chute == numero
    maior = chute > numero

    if not chute_valido:
        print("Você deve chutar um número entre 1 e 100")
        continue

    if (acertou):
        print("Você acertou!")
        break
    elif (maior):
        print("O número que você chutou é maior do que o número secreto!")
    else:
        print("O número que você chutou é menor do que o número secreto!")
