# import math

# # Função para calcular a distância entre duas coordenadas (x, y)
# def calcular_distancia(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# # Função para ler as informações das lojas do arquivo
# def ler_lojas(arquivo):
#     lojas = []
#     with open(arquivo, 'r') as f:
#         for linha in f:
#             dados = linha.strip().split(' ')
#             numero_loja = int(dados[0])
#             coordenada_x = int(dados[1])
#             coordenada_y = int(dados[2])
#             destinos = []
#             if len(dados) > 3:
#                 destinos = [int(destino) for destino in dados[3:]]
#             lojas.append((numero_loja, coordenada_x, coordenada_y, destinos))
#     return lojas

# # Função para encontrar a rota de coleta e entrega que minimize o consumo de combustível
# def encontrar_rota_lojas(arquivo):
#     lojas = ler_lojas(arquivo)
#     num_lojas = len(lojas)

#     # Matriz de distâncias entre as lojas
#     distancias = [[0] * num_lojas for _ in range(num_lojas)]

#     for i in range(num_lojas):
#         for j in range(i+1, num_lojas):
#             x1, y1 = lojas[i][1], lojas[i][2]
#             x2, y2 = lojas[j][1], lojas[j][2]
#             dist = calcular_distancia(x1, y1, x2, y2)
#             distancias[i][j] = dist
#             distancias[j][i] = dist

#     melhor_rota = []
#     menor_consumo = float('inf')

#     # Função recursiva para encontrar todas as rotas possíveis
#     def encontrar_rotas(atual, visitados, rota, combustivel):
#         nonlocal melhor_rota, menor_consumo
#         if len(rota) == num_lojas:
#             if combustivel < menor_consumo:
#                 melhor_rota = rota[:]
#                 menor_consumo = combustivel
#         else:
#             for i in range(num_lojas):
#                 if i != atual and i not in visitados:
#                     nova_rota = rota[:]
#                     nova_rota.append(i)
#                     novo_combustivel = combustivel - 0.5
#                     novo_combustivel -= distancias[atual][i]
#                     encontrar_rotas(i, visitados + [i], nova_rota, novo_combustivel)

#     # Encontrar as rotas a partir de cada loja
#     for i in range(num_lojas):
#         rota_inicial = [i]
#         visitados = [i]
#         combustivel_inicial = 10.0 - 0.5 * len(lojas[i][3])
#         encontrar_rotas(i, visitados, rota_inicial, combustivel_inicial)

#     # Imprimir a melhor rota encontrada
#     print("Melhor rota encontrada: ", end="")
#     for i in melhor_rota:
#         print(f"{lojas[i][0]}", end=" ")
#         print(f"\nMenor consumo de combustível: {menor_consumo}")

# # Exemplo de uso do algoritmo
# arquivo_lojas = "lojas.txt"
# encontrar_rota_lojas(arquivo_lojas)

# 

