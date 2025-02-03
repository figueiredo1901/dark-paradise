
print('Olá, serei seu assistente de cálculo!')
nome = input('Qual o seu nome?')
print(f'Prazer, {nome}! Por favor, insira suas respectivas notas nos campos abaixo!')
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))
resultado = (nota1+nota2+nota3+nota4)//4
print(f'{nome}, essa é sua média: {resultado:.2f} \n')