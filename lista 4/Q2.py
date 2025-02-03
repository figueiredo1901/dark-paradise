def contar_digitos(numero):
    return len(str(numero))

# Exemplo de uso
numero = int(input("Digite um número inteiro: "))
quantidade = contar_digitos(numero)
print(f"O número {numero} tem {quantidade} dígitos.")