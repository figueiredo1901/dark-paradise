salario = float(input('Digite o salário do colaborador: \n'))
salario_original = salario  

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else: 
    percentual = 5

aumento = salario * (percentual / 100)  

novo_salario = salario_original + aumento


print(f'O salário antes do reajuste era de R${salario_original:.2f}')
print(f'O percentual aplicado foi de {percentual}%')
print(f'O valor do aumento foi de R${aumento:.2f}')
print(f'O valor final do novo salário é de R${novo_salario:.2f}')
