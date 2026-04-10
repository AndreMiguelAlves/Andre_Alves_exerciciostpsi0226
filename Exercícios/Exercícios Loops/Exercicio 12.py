n = int(input("Quantos números deseja inserir? "))

soma = 0
subtracao = 0
multiplicacao = 1
divisao = 1
contador_operacoes = 0

for i in range(n):
    num = float(input(f"Digite o {i+1}º número: "))

    soma += num
    subtracao -= num
    multiplicacao *= num
    divisao /= num
    contador_operacoes += 4  

print("\nResultados:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Total de operações efetuadas: {contador_operacoes}")