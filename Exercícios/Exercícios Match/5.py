mensagem = input("Digite a mensagem: ").lower()  

if mensagem in ["olá", "bom dia"]:
    msg = 1
elif mensagem.endswith("?"):
    msg = 2
elif "tchau" in mensagem or "adeus" in mensagem:
    msg = 3
else:
    print("Mensagem genérica")

match msg:
    case 1:
        print("Saudação")
    case 2:
        print("Pergunta")
    case 3:
        print("Despedida")
    case _:
        print("Mensagem genérica")
