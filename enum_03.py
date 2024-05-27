# Estrutura enumerate (loop com índice) - formatos
lista = ["Visualizar", "Salvar", "Sair"]
for i, v in enumerate(lista):
    print("[{}]- {}".format(i, v))