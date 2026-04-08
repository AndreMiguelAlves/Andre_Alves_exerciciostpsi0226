nota = float(input("Digite a nota(0-100) : "))

if nota >= 90:
     bloco = 1
elif 70 <= nota <= 89:
     bloco = 2
elif 50 <= nota <= 69:
    bloco = 3
elif 0 <= nota < 50:
     bloco = 4
else:
    bloco = 0


match bloco:
    case 1:
        print("Excelente")
    case 2:
        print("Bom")
    case 3:
        print("Suficiente")
    case 4:
        print("Insuficiente")
