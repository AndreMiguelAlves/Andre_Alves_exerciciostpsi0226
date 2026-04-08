metodo_input = input("Digite o método (GET/POST): ").upper()
conteudo_input = input("Digite o conteúdo (pode ficar vazio): ")


requisicao = {"metodo": metodo_input, "conteudo": conteudo_input}


match requisicao:
    case {"metodo": "GET"}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c != "":
        print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": ""}:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")