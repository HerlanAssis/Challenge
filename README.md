# Challenge

![GitHub repo size](https://img.shields.io/github/repo-size/herlanassis/Challenge)
![GitHub contributors](https://img.shields.io/github/contributors/herlanassis/Challenge)
![GitHub stars](https://img.shields.io/github/stars/herlanassis/Challenge?style=social)
![GitHub forks](https://img.shields.io/github/forks/herlanassis/Challenge?style=social)
![GitHub issues](https://img.shields.io/github/issues-raw/herlanassis/Challenge?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/herlanassis?style=social)

O Challenge é um `desafio` para `testar` meus conhecimentos em `programação`.

### Problema: Lucro da ação

O senhor e-Deployer gostaria de comprar uma ação e vendê-la em um curto espaço de tempo, mas apenas se esta operação dê lucro. Para isso, é passado um array K com os valores das ações nos determinados dias, onde ele poderá escolher onde comprar e vender.
Determine o maior lucro dado esse array K de preços.

Exemplo 1:
Input: [7,1,5,3,6,4]
Output: 5
Explicação: Este valor acontece quando compramos a ação no 2o dia e a vendemos no 5o dia (6 - 1)

Exemplo 2:
Input: [7,6,4,3,1]
Output: 0
Explicação: Neste caso, não há nenhuma operação que possa ser feita que dê lucro.


## Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
* A sua versão do python é superior ou igual ao `python3`?

## Instalando Challenge

Para instalar o Challenge, siga estes passos:

```
git clone https://github.com/HerlanAssis/Challenge
```

OU [clique aqui](https://github.com/HerlanAssis/Challenge/archive/master.zip) para baixar o projeto.

## Utilizando Challenge

Para usar o Challenge, siga estes passos:

```shell
python teste.py <entrada>
```

sendo que `teste.py` respresenta o nome do script e os valores seguintes representam o array de entrada. Por exemplo:

```shell
$ python teste.py [7,1,5,3,6,4]
0

$ python teste.py [7,6,4,3,1]
0
```

## Solução

O código proposto foi:

```python
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
```

Para elaborar a solução desse problema foi preciso construir uma matriz de negociações para cada valor do array, onde cada valor representa `venda - custo`, gerando assim uma matriz `compraXvenda`. Cada coluna representa as vendas realizadas para um determinado índice. Sabendo-se que não pode existir operações entre o índice atual com o índice anterior do array.

Para o array [7,1,5,3,6,4] teremos a seuinte resposta:

7  |  1  |  5  |  3  |  6  |  4
-|-|-|-|-|-
  0  | 0 |  0  |  0  |  0  |  0  
  -6  | 4 |  -2  |  3  |  -2  |  
  -2  | 2 |  1  |  1  |    |  
  -4  | 5 |  -1  |    |    |  
  -2  | 3 |    |    |    |
  -3  |   |    |    |    |

O trecho do código equivalente a isso é:

```python
for id, value in enumerate(input):
    negotiations[str(input[id])] = []
    for idx in range(len(input)-id):
        valor_da_compra = input[id]
        valor_da_venda = input[id+idx]
        negotiations[str(input[id])].append(valor_da_venda - valor_da_compra)
```

Depois disso, foi feito uma busca em cada coluna utilizando a função `built-in` do `python` para qual coluna tem o maior valor.

```python
maximum = max(negotiations, key=negotiations.get)
```

Depois de descobri a coluna com o maior valor (lucro), basta imprimir o maior valor dessa coluna.

```python
print(max(negotiations[maximum]))
```