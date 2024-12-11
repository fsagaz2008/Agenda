class VisaoTarefa:
    @staticmethod
    def exibir_tarefas(tarefas):
        if not tarefas:
            print("Nenhuma tarefa agendada.")
            return
        
        for i, tarefa in enumerate(tarefas, 1):
            print(f"Tarefa {i}:")
            print(f"  Título: {tarefa.titulo}")
            print(f"  Descrição: {tarefa.descricao}")
            print()

    @staticmethod
    def obter_detalhes_tarefa():
        titulo = input("Digite o título da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        return titulo, descricao
