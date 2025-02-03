numero_c = input('Insira os dígitos do cartão: \n')
numero_c = numero_c.replace(" ", "")

ocultar = "**** **** ****" + numero_c[-4:]
print(f"Número do cartão oculto: {ocultar} \n")