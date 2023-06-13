def resolver_problema_branch_and_bound(lojas, capacidade_caminhao):
    melhor_distancia = math.inf
    melhor_caminho = None

    def backtrack(caminho, carga, distancia_total):
        nonlocal melhor_distancia, melhor_caminho

        if len(caminho) == len(lojas):
            if distancia_total < melhor_distancia:
                melhor_distancia = distancia_total
                melhor_caminho = caminho.copy()
            return

        atual = caminho[-1].numero

        for proxima_loja in lojas:
            if proxima_loja.numero not in caminho and proxima_loja.numero != atual:
                nova_carga = carga
                nova_distancia = distancia_total
                if proxima_loja.numero in lojas[atual].destinos:
                    nova_carga -= 1
                else:
                    nova_carga += 1

                if nova_carga <= capacidade_caminhao and nova_distancia + calcular_distancia(lojas[atual].x, lojas[atual].y, proxima_loja.x, proxima_loja.y) < melhor_distancia:
                    nova_distancia += calcular_distancia(lojas[atual].x, lojas[atual].y, proxima_loja.x, proxima_loja.y)
                    backtrack(caminho + [proxima_loja], nova_carga, nova_distancia)

    backtrack([lojas[0]], 0, 0)
    return melhor_caminho, melhor_distancia

# Exemplo de uso
lojas = []
with open('lojas.txt', 'r') as arquivo:
    for linha in arquivo:
        dados = linha.split()
        numero = int(dados[0])
        x = int(dados[1])
        y = int(dados[2])
        destinos = [int(destino) for destino in dados[3:]]
        lojas.append(Loja(numero, x, y, destinos))

capacidade_caminhao = 3
melhor_caminho, melhor_distancia = resolver_problema_branch_and_bound(lojas, capacidade_caminhao)
plotar_animacao(lojas, melhor_caminho, melhor_distancia)
