N = int(input("Quantas notas você deseja inserir? "))

if N <= 0:
    print("O número de notas deve ser maior que zero.")
else:
    soma = 0

    for i in range(N):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        soma += nota

    media = soma / N
    print(f"A média das {N} notas é: {media:.2f}")
