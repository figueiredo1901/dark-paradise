def reverso(numero):
    return int(str(numero)[::-1])

num = int(input("Digite um número inteiro: "))
print(f"O reverso de {num} é {reverso(num)}")
