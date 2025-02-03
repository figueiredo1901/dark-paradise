km = int(input('Por favor, insira a quantidade exata de km percorridos: \n'))
dias = float(input('Informe a quantidade de dias que o veículo foi alugado: \n'))

resultado_1 = km*0.20
resultado_2 = dias*90
valor_final = resultado_1 + resultado_2
print(f'O valor total a pagar é de R$ {valor_final:.2f} \n')