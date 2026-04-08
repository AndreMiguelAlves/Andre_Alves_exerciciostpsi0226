def contar_minusculas(palavra):
    
    contador = 0
    for caracter in palavra:
        
        if 'a' <= caracter <= 'z':
            contador += 1
    return contador

def ordenar_minusculas(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            contagem_atual = contar_minusculas(lista[j])
            contagem_proxima = contar_minusculas(lista[j + 1])
            
            if contagem_atual > contagem_proxima:
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    return lista


palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
resultado = ordenar_minusculas(palavras)

print(f"Resultado ordenado: {resultado}")