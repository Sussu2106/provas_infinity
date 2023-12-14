alunos = {}

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    alunos[matricula] = nome
    print(f"Aluno {nome} adicionado com sucesso!\n")

def remover_aluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso!\n")
    else:
        print("Número de matrícula não encontrado.\n")

def visualizar_alunos():
    if alunos:
        print("Lista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
    else:
        print("Nenhum aluno registrado.\n")

while True:
    print("Escolha uma opção:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        remover_aluno()
    elif opcao == '3':
        visualizar_alunos()
    elif opcao == '4':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
