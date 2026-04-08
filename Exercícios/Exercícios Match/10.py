j1 = input("Jogador 1: ").lower()
j2 = input("Jogador 2: ").lower()

match j1:
    case "pedra":
        if j2 == "pedra":
            print("Empate")
        elif j2 == "tesoura":
            print("Jogador 1 venceu")
        elif j2 == "papel":
            print("Jogador 2 venceu")
        else:
            print("Jogada inválida")
    case "papel":
        if j2 == "papel":
            print("Empate")
        elif j2 == "pedra":
            print("Jogador 1 venceu")
        elif j2 == "tesoura":
            print("Jogador 2 venceu")
        else:
            print("Jogada inválida")
    case "tesoura":
        if j2 == "tesoura":
            print("Empate")
        elif j2 == "papel":
            print("Jogador 1 venceu")
        elif j2 == "pedra":
            print("Jogador 2 venceu")
        else:
            print("Jogada inválida")
    case _:
        print("Jogada inválida")