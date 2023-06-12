from vpython import *

def plotar_animacao_vpython(lojas, caminho, distancia_total):
    scene = canvas(title="Viagens do Caminhão", width=800, height=600)

    # Criação dos objetos gráficos das lojas
    lojas_grafico = []
    for loja in lojas:
        sphere(pos=vector(loja.x, loja.y, 0), radius=10, color=color.red)
        lojas_grafico.append(label(pos=vector(loja.x, loja.y, 0), text=str(loja.numero)))

    # Animação das viagens do caminhão
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i+1]

        arrow(pos=vector(origem.x, origem.y, 0), axis=vector(destino.x - origem.x, destino.y - origem.y, 0), color=color.blue, shaftwidth=1)

        rate(1)  # Taxa de atualização da animação (1 frame por segundo)

    # Exibição do resultado final
    scene.append_to_caption(f"\nDistância total: {distancia_total:.2f} km")
    scene.waitfor('click')  # Aguarda um clique para encerrar a animação

# Exemplo de uso


capacidade_caminhao = 3
melhor_caminho, melhor_distancia = resolver_problema_b(lojas, capacidade_caminhao)
plotar_animacao_vpython(lojas, melhor_caminho, melhor_distancia)
