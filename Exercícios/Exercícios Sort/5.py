def ordenar_lista(lista):
    
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def agrupar_e_ordenar(lista_palavras):
    dicionario = {}
    
    
    for palavra in lista_palavras:
       
        letra = palavra[0].lower()
        
        if letra not in dicionario:
            dicionario[letra] = []
        
        dicionario[letra].append(palavra)
    
    
    for chave in dicionario:
        dicionario[chave] = ordenar_lista(dicionario[chave])
        
    return dicionario


palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
resultado = agrupar_e_ordenar(palavras)


print(resultado)

