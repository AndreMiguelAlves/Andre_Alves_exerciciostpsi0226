def ordenar_letras(palavra):
    caracteres = list(palavra)
    
    n = len(caracteres)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            if caracteres[j] > caracteres[j + 1]:
                caracteres[j], caracteres[j + 1] = caracteres[j + 1], caracteres[j]
    
    palavra_ordenada = "".join(caracteres)
    
    return palavra_ordenada

entrada = "algoritmo"
resultado = ordenar_letras(entrada)

print(f"Palavra original: {entrada}")
print(f"Resultado esperado: {resultado}")