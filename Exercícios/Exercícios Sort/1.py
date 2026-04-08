def ordenar_palavras(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):   
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


frutas = ["banana", "uva", "abacaxi", "laranja"]
resultado = ordenar_palavras(frutas)

print(f"Lista ordenada: {resultado}")