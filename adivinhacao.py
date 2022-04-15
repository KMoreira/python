print("bem vindo ao jogo da advinhação!")

numero_secreto = 32

chute_str = input("Digite seu numero: ")
chute = int(chute_str)

if(numero_secreto == chute):
    print("Voce acertou\n")
else:
    print("Voce errou\n")

