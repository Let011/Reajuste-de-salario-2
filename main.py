
salario = float(input('Informe o salario: '))
aumento = float(input('informe a porcentagem de aumento: '))
aumento = (aumento / 100)
reajuste = (salario * aumento) 
salario = salario + reajuste

print('O salario foi reajustado para: ', salario)
