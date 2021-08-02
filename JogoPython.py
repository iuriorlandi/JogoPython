def EscreveCabecalho():
    print("********************")
    print("Jogo de adivinhação.")
    print("********************")

EscreveCabecalho()

numero = 52

numero_digitado = int(input())

if(numero == numero_digitado):
    print("Você acertou!")
else:
    print("Você errou!")

input()