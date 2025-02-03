nota_minima = 0
nota_maxima = 10

while True:
    try:
        entrada = int(input(f"Digite uma nota entre {nota_minima} e {nota_maxima}: ")) 
        if nota_minima <= entrada <= nota_maxima: 
            print(f"Você digitou {entrada}, que está dentro do intervalo!")
            break  
        else:
            print(f"Erro! A nota precisa estar entre {nota_minima} e {nota_maxima}. Tente novamente.")
    except ValueError:
        print("Erro! Você precisa digitar um número válido.")
