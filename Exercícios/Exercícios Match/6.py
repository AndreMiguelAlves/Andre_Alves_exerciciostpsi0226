status_input = input("Digite o status do servidor (ok/erro): ")
tempo_input = int(input("Digite o tempo de resposta do servidor em ms: "))

servidor = {"status":status_input, "tempo_resposta":tempo_input}

if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
    estado = 1
elif servidor["status"] == "ok":
    estado = 2
elif servidor["status"] == "erro":
    estado = 3
else:
    print("Estado desconhecido")

match estado:
    case 1:
        print("Servidor lento")
    case 2:
        print("Servidor ativo")
    case 3:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")