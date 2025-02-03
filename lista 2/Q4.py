nome = input('Insira seu nome: \n')
sexo = input('Insira seu gênero: \n')
valor = float(input('Insira o valor adquirido: \n'))

if sexo == "homem" or sexo == "Homem":
    percentual = 5
elif sexo == "mulher" or sexo == "Mulher":
    percentual = 13
else:
    percentual = 0
    
valor_desconto = valor * (percentual/100)
valor_final = valor - valor_desconto

print(f"Você recebeu um desconto de {percentual}%. O valor final é de R${valor_final:.2f} reais.")