from vertice import Vertice

class Grafo:
    def __init__(self):
        self.quantidade_estacoes = 0
        self.linha_metro = {}

    def adicionar_estacao(self, estacao):
        self.quantidade_estacoes += 1
        self.linha_metro[estacao] = []

    def remover_estacao(self, estacao):
        if estacao in self.linha_metro.keys():
            for ligacoes in self.linha_metro.values():
                if estacao in ligacoes:
                    ligacoes.remove(estacao)

            del self.linha_metro[estacao]
            self.quantidade_estacoes -= 1

    def __verifica_conexao(self, estacao1, estacao2):
        for estacoes in self.linha_metro[estacao1]:
            if estacao2 == estacoes:
                return True

        return False

    def adicionar_ligacoes(self, estacao1, estacao2):
        if estacao1 not in self.linha_metro.keys():
            print(f"Estação {estacao1.nome} inexistente")
            return
                                                    
        if estacao2 not in self.linha_metro.keys():
            print(f"Estação {estacao2.nome} inexistente")
            return

        if self.__verifica_conexao(estacao1, estacao2):
            print(f"Conexão entre {estacao1.nome} e {estacao2.nome} já existe")
            return
    
        self.linha_metro[estacao1].append(estacao2)
        self.linha_metro[estacao2].append(estacao1)

    def remover_ligacoes(self, estacao1, estacao2):
        if estacao1 not in self.linha_metro.keys():
            return

        if estacao2 not in self.linha_metro.keys():
            return

        if not self.__verifica_conexao(estacao1, estacao2):
            return

        self.linha_metro[estacao1].remove(estacao2)
        self.linha_metro[estacao2].remove(estacao1)


    def mostrar_linha(self):
        for estacao, conexoes in self.linha_metro.items():
            print(f"Estação {estacao.nome}: {conexoes}")
