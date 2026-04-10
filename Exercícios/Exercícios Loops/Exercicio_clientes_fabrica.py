base_dados = []

while True:
    print("\n--- MENU FÁBRICA ---")
    print("1. Inserir Cliente")
    print("2. Listar Todos")
    print("3. Busca Direta (Por ID)") 
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id_cliente = len(base_dados) + 1
        nome = input("Nome: ")
        morada = input("Morada: ") 
        tel = input("Telefone: ")  
        nif = input("NIF: ")       

        
        try:
            valor = float(input("Valor da compra: "))
        except ValueError:
            print("Erro: Insira um valor numérico!")
            continue 

        if 100 <= valor <= 200:
            valor_final = valor * 0.95
        elif 200 < valor <= 500:
            valor_final = valor * 0.90
        elif valor > 500:
            valor_final = valor * 0.85
        else:
            valor_final = valor

        novo_cliente = {
            "id": id_cliente, 
            "nome": nome, 
            "morada": morada,
            "tel": tel,
            "nif": nif,
            "compra": valor, 
            "valor final": valor_final
        }
        base_dados.append(novo_cliente)
        print(f"Cliente {nome} guardado com ID {id_cliente}!")

    elif opcao == "2":
        print("\n--- LISTAGEM ---")
        for c in base_dados:     
            print(f"ID: {c['id']} | Nome: {c['nome']} | NIF: {c['nif']} | Total: {c['valor final']}€")
            input("Pressione Enter para ver o próximo...") 

    elif opcao == "3":
        try:
            busca_id = int(input("Qual o número do cliente? "))
            encontrado = False
            for c in base_dados:
                if c["id"] == busca_id:
                    print(f"\nCliente Encontrado:\nNome: {c['nome']}\nNIF: {c['nif']}\nDívida Final: {c['valor final']}€")
                    encontrado = True
                    break
            if not encontrado:
                print("Cliente não encontrado.")
        except ValueError:
            print("ID inválido.")

    elif opcao == "4":
        print("A fechar programa...")
        break