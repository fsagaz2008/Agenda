from modelo import Tarefa, ModeloTarefa
from visao import VisaoTarefa

class ControladorTarefa:
    def __init__(self):
        self.modelo = ModeloTarefa()
        self.visao = VisaoTarefa()

    def adicionar_tarefa(self):
        titulo, descricao = self.visao.obter_detalhes_tarefa()
        tarefa = Tarefa(titulo, descricao)
        self.modelo.adicionar_tarefa(tarefa)

    def exibir_tarefas(self):
        tarefas = self.modelo.obter_tarefas()
        self.visao.exibir_tarefas(tarefas)
