#Projeto Gerenciador de Tarefas Simples
#Menu principal:
#O programa exibe um menu para o usuário escolher entre:
#Adicionar tarefa
#Exibir tarefas
#Marcar tarefa como concluída
#Sair

tarefas = []
entrada = True

while entrada:
    print("Escolha uma das opções abaixo")
    print("[1] - Adicionar nova tarefa")
    print("[2] - Exibir tarefas")
    print("[3] - Marcar tarefa como concluída")
    print("[4]  Sair")
    entrada = input("Opção: ")
    if entrada == "1":
        print("Digite a tarefa que você quer adicionar: ")
        tarefa = input("Tarefa: ")
        tarefas.append(tarefa)
    if entrada == "2":
        for item in tarefas:
            print(item)
    if entrada == "3":
        for item in tarefas:
            print(item)
        print("Dessas tarefas, quais foram concluidas ?")    
        concluidas = input("As tarefas concluidas são: ")
        if concluidas == "concluidas":
            print("Tarefa concluida com sucesso")
    if entrada == "4":
        etradada = False
        break