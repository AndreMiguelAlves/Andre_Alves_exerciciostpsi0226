
lista = []


def inserir(lista):
    nome = input("nome: ")
    idade = input("idade: ")
    curso = input("curso: ")
    aluno = {
        "nome": nome, 
        "idade": idade,
        "curso":curso
    }
    lista.append(aluno)
    
    print("Aluno adicionado")

def listar(lista):
    for aluno in lista:
        print(f"Nome: {aluno['nome']}") 
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print("-"*15)
while True:
    print("1- Inserir aluno")
    print("2- Listar alunos")
    opc = (input("Opção : "))
    
    if opc == "1":
        inserir(lista)

    elif opc == "2":
        listar(lista)
