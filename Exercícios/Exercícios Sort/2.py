def ordenar_inverso(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            palavra_atual = lista[j].lower()
            proxima_palavra = lista[j + 1].lower()
            if palavra_atual < proxima_palavra:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    return lista

palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]
resultado = ordenar_inverso(palavras)

print(f"Resultado esperado: {resultado}")