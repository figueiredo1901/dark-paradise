print("Lojas Quase Dois - Tabela de Preços")

preco_unitario = 1.99

for i in range(1, 51):
    total = i * preco_unitario
    print(f"{i} - R$ {total:.2f}")
