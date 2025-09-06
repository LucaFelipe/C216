alunos = []
contador_curso = {}  # dicionário para controlar a sequência por curso

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input("Digite o curso do aluno: ").strip()
    
    if curso not in contador_curso:
        contador_curso[curso] = 1
    else:
        contador_curso[curso] += 1
    
    matricula = f"{curso[:3].upper()}{contador_curso[curso]}"  
    
    alunos.append({
        "nome": nome,
        "email": email,
        "curso": curso,
        "matrícula": matricula
    })
    
    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")

def listar_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso'], "Matrícula": aluno['matrícula']}")

def atualizar_aluno():
    nome = input("Digite o nome do aluno a ser atualizado: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            aluno["email"] = input("Digite o novo e-mail do aluno: ")
            aluno["curso"] = input("Digite o novo curso do aluno: ")
            aluno["matrícula"] = input("Digite a nova matrícula do aluno: ")
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

def remover_aluno():
    nome = input("Digite o nome do aluno a ser removido: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return
    print("Aluno não encontrado.")
    
def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Atualizar Professor")
        print("4. Remover Professor")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_aluno()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()