from vpython import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Loja
from Leitor import Leitor
import Metodos

# def gerar_solucoes_possiveis(lojas, capacidade_caminhao):
#     solucoes = []

#     def backtrack(caminho, carga, distancia_total):
#         if len(caminho) == len(lojas):
#             solucoes.append((caminho.copy(), distancia_total))
#             return

#         atual = caminho[-1].numeroLoja

#         for proxima_loja in lojas:
#             if proxima_loja.numeroLoja not in caminho and proxima_loja.numeroLoja != atual:
#                 nova_carga = carga
#                 nova_distancia = distancia_total
#                 if proxima_loja.numeroLoja in lojas[atual].listaDeEntrega:
#                     nova_carga -= 1
#                 else:
#                     nova_carga += 1

#                 if nova_carga <= capacidade_caminhao:
#                     nova_distancia += Metodos.calcular_distancia(lojas[atual].x, lojas[atual].y, proxima_loja.x, proxima_loja.y)
#                     novo_custo = Metodos.calcular_gasto_combustivel(nova_distancia, nova_carga)
#                     backtrack(caminho + [proxima_loja], nova_carga, nova_distancia, novo_custo)

#     backtrack([lojas[0]], 0, 0)
#     return solucoes

# def plotar_animacao(lojas, caminho, distancia_total):
#     fig, ax = plt.subplots()

#     def update(frame):
#         ax.cla()
#         ax.set_xlim(0, 500)
#         ax.set_ylim(0, 500)
#         ax.set_title(f"Distância total: {distancia_total:.2f} km")

#         for loja in lojas:
#             ax.annotate(loja.numeroLoja, (loja.x, loja.y))

#         for i in range(len(caminho) - 1):
#             ax.plot([caminho[i].x, caminho[i+1].x], [caminho[i].y, caminho[i+1].y], 'b-')

#     ani = animation.FuncAnimation(fig, update, frames=len(caminho), interval=100)
#     plt.show()

# def resolver_problema_forca_bruta(lojas, capacidade_caminhao):
#     solucoes_possiveis = gerar_solucoes_possiveis(lojas, capacidade_caminhao)
   
#     melhor_solucao = min(solucoes_possiveis, key=lambda x: x[2])
#     caminho, distancia_total = melhor_solucao

#     plotar_animacao(lojas, caminho,distancia_total)
# def gerar_solucoes_possiveis(lojas, capacidade_caminhao):
#     solucoes = []

#     def backtrack(caminho, carga, custo_total):
#         if len(caminho) == len(lojas):
#             solucoes.append((caminho.copy(), custo_total))
#             return

#         atual = caminho[-1].numero

#         for proxima_loja in lojas:
#             if proxima_loja.numero not in caminho and proxima_loja.numero != atual:
#                 nova_carga = carga
#                 novo_custo = custo_total
#                 if proxima_loja.numero in lojas[atual].destinos:
#                     nova_carga -= 1
#                 else:
#                     nova_carga += 1

#                 if nova_carga <= capacidade_caminhao:
#                     distancia = Metodos.calcular_distancia(lojas[atual].x, lojas[atual].y, proxima_loja.x, proxima_loja.y)
#                     novo_custo += Metodos.calcular_gasto_combustivel(distancia, nova_carga)
#                     backtrack(caminho + [proxima_loja], nova_carga, novo_custo)

#     backtrack([lojas[0]], 0, 0)
#     return solucoes
def gerar_solucoes_possiveis(lojas, capacidade_caminhao):
    solucoes = []

    def backtrack(caminho, carga, custo_total):
        if len(caminho) == len(lojas) and caminho:
            solucoes.append((caminho.copy(), custo_total))
            return

        atual = caminho[-1].numero if caminho else None

        for proxima_loja in lojas:
            if proxima_loja.numero not in caminho and proxima_loja.numero != atual:
                nova_carga = carga
                novo_custo = custo_total
                if proxima_loja.numero in lojas[atual].destinos:
                    nova_carga -= 1
                else:
                    nova_carga += 1

                if nova_carga <= capacidade_caminhao:
                    distancia = Metodos.calcular_distancia(lojas[atual].x, lojas[atual].y, proxima_loja.x, proxima_loja.y)
                    novo_custo += Metodos.calcular_gasto_combustivel(distancia, nova_carga)
                    backtrack(caminho + [proxima_loja], nova_carga, novo_custo)

    backtrack([lojas[0]], 0, 0)
    return solucoes

def plotar_animacao(lojas, caminho, distancia_total):
    fig, ax = plt.subplots()

    def update(frame):
        ax.cla()
        ax.set_xlim(0, 500)
        ax.set_ylim(0, 500)
        ax.set_title(f"Distância total: {distancia_total:.2f} km")

        for loja in lojas:
            ax.annotate(loja.numero, (loja.x, loja.y))

        for i in range(len(caminho) - 1):
            ax.plot([caminho[i].x, caminho[i+1].x], [caminho[i].y, caminho[i+1].y], 'b-')

    ani = animation.FuncAnimation(fig, update, frames=len(caminho), interval=1000)
    plt.show()

def resolver_problema_forca_bruta(lojas, capacidade_caminhao):
    solucoes_possiveis = gerar_solucoes_possiveis(lojas, capacidade_caminhao)
    print(solucoes_possiveis)
    melhor_solucao = min(solucoes_possiveis, key=lambda x: x[1])
    caminho, custo_total = melhor_solucao
    for i in (caminho):
        print(i.numero, custo_total)

    plotar_animacao(lojas, caminho, custo_total)


# Exemplo de uso
lojas = Leitor("lojas.txt")

capacidade_caminhao = 2

resolver_problema_forca_bruta(lojas,capacidade_caminhao)



# def plotar_animacao_vpython(lojas, caminho, distancia_total):
#     scene = canvas(title="Viagens do Caminhão", width=800, height=600)

#     # Criação dos objetos gráficos das lojas
#     lojas_grafico = []
#     for loja in lojas:
#         sphere(pos=vector(loja.x, loja.y, 0), radius=10, color=color.red)
#         lojas_grafico.append(label(pos=vector(loja.x, loja.y, 0), text=str(loja.numero)))

#     # Animação das viagens do caminhão
#     for i in range(len(caminho) - 1):
#         origem = caminho[i]
#         destino = caminho[i+1]

#         arrow(pos=vector(origem.x, origem.y, 0), axis=vector(destino.x - origem.x, destino.y - origem.y, 0), color=color.blue, shaftwidth=1)

#         rate(1)  # Taxa de atualização da animação (1 frame por segundo)

#     # Exibição do resultado final
#     scene.append_to_caption(f"\nDistância total: {distancia_total:.2f} km")
#     scene.waitfor('click')  # Aguarda um clique para encerrar a animação

# Exemplo de uso
# melhor_caminho, melhor_distancia = resolver_problema_forca_bruta(lojas, capacidade_caminhao)
# plotar_animacao_vpython(lojas, melhor_caminho, melhor_distancia)