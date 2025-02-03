morango_quant = float(input('Insira a quantidade em KG de morango: \n'))
maça_quant = float(input('Insira a quantidade em KG de maçãs: \n'))

if morango_quant <= 5:
    preço_m = 2.50
else:
    preço_m = 2.20

if maça_quant <= 5:
    preço_mm = 1.80
else:
    preço_mm = 1.50

total_mo = morango_quant * preço_m
total_ma = maça_quant * preço_mm
valor_total = total_mo + total_ma

peso_total = morango_quant + maça_quant
if peso_total > 8 or valor_total > 25:
    desconto = 10

novo_valor = valor_total * (desconto/100)
valor_final = valor_total - novo_valor

print(f'O total a pagar é de R${valor_final:.2f}')