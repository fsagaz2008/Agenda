from controlador import ControladorTarefa

def main():
    controlador = ControladorTarefa()
    
    while True:
        print("1. Adicionar Tarefa")
        print("2. Exibir Tarefas")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            controlador.adicionar_tarefa()
        elif escolha == '2':
            controlador.exibir_tarefas()
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
