from vertice import Vertice
from grafos import Grafo

estacao1 = Vertice("Sé")
estacao2 = Vertice("Luz")

print(estacao1.nome)
print(estacao2.nome)

linha_metro = Grafo()

linha_metro.adicionar_estacao(estacao1)
linha_metro.adicionar_estacao(estacao2)
linha_metro.mostrar_linha()
