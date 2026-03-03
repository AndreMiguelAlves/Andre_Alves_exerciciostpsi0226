'''
==========================================
OPERADORES EM PYTHON
Aritméticos | Decisão | Lógicos | IF
==========================================
'''

# ---------------------------------
# OPERADORES ARITMÉTICOS
# ---------------------------------

# +  -> soma
# -  -> subtracção
# /  -> divisão
# *  -> multiplicação
# %  -> resto da divisão (módulo)
# ** -> potência (exponencial)

total = 0
num1 = 0
num2 = 0

# INPUT DE VALORES
num1 = int(input("Insira o número 1: "))
num2 = int(input("Insira o número 2: "))

# Soma
total = num1 + num2
print(f"Soma: {total}")

# Subtracção
total = num1 - num2
print(f"Subtracção: {total}")

# Divisão
total = num1 / num2
print(f"Divisão: {total}")

# Multiplicação
total = num1 * num2
print(f"Multiplicação: {total}")

# Resto da divisão
total = num1 % num2
print(f"Resto da divisão: {total}")

# Potência
total = num1 ** num2
print(f"Potência: {total}")


# ---------------------------------
# OPERADORES DE DECISÃO (COMPARAÇÃO)
# ---------------------------------

# ==  igualdade
# !=  diferente
# >   maior que
# <   menor que
# >=  maior ou igual
# <=  menor ou igual

# Uma expressão devolve sempre True ou False
# Exemplo:
# val1 == val2  -> True ou False


# ---------------------------------
# OPERADORES LÓGICOS
# ---------------------------------

# and -> E (ambas as condições têm de ser verdadeiras)
# or  -> OU (apenas uma precisa de ser verdadeira)
# not -> negação

# Exemplo lógico:
# True and False  -> False
# True or False   -> True


# ---------------------------------
# IF SIMPLES
# ---------------------------------

val1 = 2
val2 = 3

if val1 > val2:
    print("val1 é o maior")
else:
    print("val2 é o maior")

    # ---------------------------------
# EXERCÍCIO: ENCONTRAR O MAIOR E O MENOR
# ---------------------------------
# Forma organizada e correcta

if val1 >= val2 and val1 >= val3:
    maior = val1
elif val2 >= val1 and val2 >= val3:
    maior = val2
else:
    maior = val3

if val1 <= val2 and val1 <= val3:
    menor = val1
elif val2 <= val1 and val2 <= val3:
    menor = val2
else:
    menor = val3

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")


# ---------------------------------
# MATCH CASE (Python 3.10+)
# ---------------------------------

print("\nMenu:")
print("1 - Bom dia")
print("2 - Boa noite")
print("3 - Sair")

opc = input("Escolha uma opção: ")

match opc:
    case "1":
        print("Bom dia")
    case "2":
        print("Boa noite")
    case "3":
        print("A sair do programa...")
    case _:
        print("Opção inválida")


        '''
==========================================
COMENTÁRIOS E TIPOS DE DADOS EM PYTHON
==========================================
'''

# Comentário de uma linha utiliza o símbolo #

# ---------------------------------
# OUTPUT (SAÍDA) PARA A CONSOLA
# ---------------------------------

print("Hello World TPSI0226")


# ---------------------------------
# INT (Número Inteiro)
# ---------------------------------

tel = 9   # número inteiro (int)
print("\nTipo da variável tel:")
print(type(tel))
print("Valor de tel:")
print(tel)

# Python é uma linguagem de tipagem dinâmica
# A mesma variável pode mudar de tipo automaticamente

tel = "9"   # agora é uma STRING (texto), já não é número

# Atenção:
# "9" NÃO tem valor 57.
# Só teria valor 57 se utilizássemos: ord("9")

print("\nTipo da variável tel após alteração:")
print(type(tel))
print("Novo valor de tel:")
print(tel)


# ---------------------------------
# FLOAT (Número Decimal)
# ---------------------------------

med = 2.3
print("\nTipo da variável med:")
print(type(med))
print("Valor de med:")
print(med)


# ---------------------------------
# STRING (Texto)
# ---------------------------------

nom = "Dario"
print("\nTipo da variável nom:")
print(type(nom))
print("Valor de nom:")
print(nom)


# ---------------------------------
# BOOLEAN (Verdadeiro ou Falso)
# ---------------------------------

flag = True
print("\nTipo da variável flag:")
print(type(flag))
print("Valor de flag:")
print(flag)


# ---------------------------------
# LISTA []
# ---------------------------------
# Pode guardar vários tipos de dados
# É MUTÁVEL (pode ser alterada)

lista = [1, "dario", 4.4, False, 9]

print("\nTipo da variável lista:")
print(type(lista))
print("Conteúdo da lista:")
print(lista)


# ---------------------------------
# TUPLO ()
# ---------------------------------
# Parecido com a lista, mas é IMUTÁVEL
# Não pode ser alterado depois de criado

tuplo = (1, 3, 4, 6)

print("\nTipo da variável tuplo:")
print(type(tuplo))
print("Conteúdo do tuplo:")
print(tuplo)
