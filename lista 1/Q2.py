peso = float(input('Digite o peso dos peixes: \n'))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'O excesso de peso é de {excesso} kg \n')
    print(f'O valor da multa é de R${multa:.2f} \n')
else:
    print("Se não há excesso de peso, portanto não há multa! \n")

