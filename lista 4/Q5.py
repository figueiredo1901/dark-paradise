import math

def calcular_raiz(valor):
    return math.isqrt(valor)

N = int(input("Quantos números deseja inserir? "))
numeros = list(map(int, input("Digite os números separados por espaço: ").split()))

for num in numeros:
    print(calcular_raiz(num))