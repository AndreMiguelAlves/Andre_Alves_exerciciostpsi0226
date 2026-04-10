for codigo in range(256):  
    print(f"{codigo} - {chr(codigo)}", end="\t")

    
    if (codigo + 1) % 20 == 0:
        print()
        resposta = input("Quer continuar? (s/n): ").lower()
        if resposta != "s":
            break