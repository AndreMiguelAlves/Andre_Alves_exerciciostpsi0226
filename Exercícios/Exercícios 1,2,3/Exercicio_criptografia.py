def calcular_valor_chave(chave: str) -> int:
    
    soma = 0
    for letra in chave:
        soma += ord(letra)
    return soma

def criptografar(mensagem: str, chave: str):
    if not chave:
        return "Erro: A chave não pode estar vazia."
    
    valor_chave = calcular_valor_chave(chave)
    resultado = []
    
    for caractere in mensagem:
        codigo_original = ord(caractere)
        novo_codigo = 32 + (codigo_original - 32 + valor_chave) % 95
        resultado.append(novo_codigo)
    
    return resultado

def descriptografar(codigos: list, chave: str) -> str:
    if not chave:
        return "Erro: A chave não pode estar vazia."
    
    valor_chave = calcular_valor_chave(chave)
    mensagem_original = ""
    
    for codigo in codigos:
        original = 32 + (codigo - 32 - valor_chave) % 95
        mensagem_original += chr(original)
    
    return mensagem_original


mensagens_guardadas = []

while True:
    print("\n--- Sistema de Criptografia ---")
    print("1- Criptografar")
    print("2- Descriptografar e Listar")
    print("0- Sair")
    opc = input("Opção: ")

    if opc == "1":
        msg = input("Mensagem: ")
        key = input("Chave (string): ")
        if key:
            codigos = criptografar(msg, key)
            mensagens_guardadas.append(codigos)
            print(f"Criptografado com sucesso: {codigos}")
        else:
            print("Erro: Chave vazia!")

    elif opc == "2":
        if not mensagens_guardadas:
            print("Nenhuma mensagem guardada.")
        else:
            key = input("Chave para descriptografar: ")
            print("\n--- Mensagens Recuperadas ---")
            for cod in mensagens_guardadas:
                print(descriptografar(cod, key))
    
    elif opc == "0":
        break