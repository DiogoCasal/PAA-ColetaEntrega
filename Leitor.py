from Loja import Loja
def Leitor(nomeArquivo):
  f = open(nomeArquivo, "r")
  #numero de lojas no arquivo

  lojas = list()
  # Lê todas as linhas do arquivo e salva em uma lista
  linhas = f.readlines()

  linhas = [x.strip() for x in linhas]
  # print(linhas)
  for x in range (len(linhas)):
    dados = linhas[x].split()
    numero_loja = int(dados[0])
    x = int(dados[1])
    y = int(dados[2])
    destinos = [int(destino) for destino in dados[3:]]
    lojas.append(Loja(numero_loja, x, y, destinos))

  f.close()
  return lojas

# print(Leitor("lojas.txt"))
