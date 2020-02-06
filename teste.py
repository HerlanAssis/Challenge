import sys
import re

array = sys.argv[1]

# retira apenas os números do array
# utilizando uma expressão regular do python
input = [int(i) for i in re.findall("\d", array)]

# dicionário vazio onde cada chave será
# um item do array de entrada
negotiations = {}

for id, value in enumerate(input):
    # será inicializado um array vazio para cada
    # item do array de entrada
    negotiations[str(input[id])] = []

    indice_atual = len(input)-id
    for idx in range(indice_atual):
        valor_da_compra = input[id]
        valor_da_venda = input[id+idx]
        negotiations[str(input[id])].append(valor_da_venda - valor_da_compra)

maximum = max(negotiations, key=negotiations.get)

print(max(negotiations[maximum]))