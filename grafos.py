class Grafo:
    def __init__(self):
        self.quantidade_estacoes = 0
        self.linha_metro = {}

    def adicionar_estacao(estacao):
        self.quantidade_estacoes += 1
        self.linha_metro.update(estacao: [])

    def remover_estacao(estacao):
        if estacao in self.linha_metro.keys():
            del self.linha_metro[estacao]
