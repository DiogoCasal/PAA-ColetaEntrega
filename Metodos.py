import math

def calcular_distancia(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calcular_gasto_combustivel(distancia, num_produtos):
    rendimento = 10 - 0.5 * num_produtos
    consumo = distancia / rendimento
    return consumo



def encontrar_proxima_loja(lojas, atual, visitadas):
    menor_distancia = math.inf
    proxima_loja = None
        
    for loja in lojas:
        if loja.numeroloja not in visitadas and loja.numeroloja != atual:
            distancia = calcular_distancia(loja.x, loja.y, lojas[atual].x, lojas[atual].y)
            if distancia < menor_distancia:
                menor_distancia = distancia
                proxima_loja = loja

        return proxima_loja
 

# def resolver_problema(lojas, capacidade_caminhao):
#     visitadas = set()
#     caminho = [lojas[0]]
#     carga = 0
#     distancia_total = 0
#     custo_total = 0

#     while len(visitadas) < len(lojas) - 1:
#         atual = caminho[-1].numeroloja
#         proxima_loja = encontrar_proxima_loja(lojas, atual, visitadas)

#         if proxima_loja is None:
#             break

#         visitadas.add(proxima_loja.numeroloja)
#         caminho.append(proxima_loja)

#         if proxima_loja.numeroloja in lojas[atual].listaDeEntrega:
#             carga -= 1
#         else:
#             carga += 1

#         if carga > capacidade_caminhao:
#             distancia_entrega = calcular_distancia(lojas[atual].x, lojas[atual].y, lojas[0].x, lojas[0].y)
#             distancia_total += distancia_entrega
#             gasto_combustivel = calcular_gasto_combustivel(distancia_entrega, carga)
#             distancia_total += gasto_combustivel
#             carga = 0

#     distancia_volta = calcular_distancia(lojas[caminho[-1].numeroloja].x, lojas[caminho[-1].numeroloja].y, lojas[0].x, lojas[0].y)
#     distancia_total += distancia_volta
#     gasto_combustivel = calcular_gasto_combustivel(distancia_volta, carga)
#     distancia_total += gasto_combustivel

#     return caminho, distancia_total