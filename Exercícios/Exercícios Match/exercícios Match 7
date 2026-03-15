produto = {"categoria": "eletrónico", "preco": 1500}

match produto:
    case {"categoria": "eletrónico", "preco": preco} if preco > 1000:
        print("Produto de luxo")
    case {"categoria": "eletrónico", "preco": preco} if preco <= 1000:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")