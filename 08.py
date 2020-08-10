#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_da_hora_trabalhada = float(input("Digite o valor da hora trabalhada"))
numero_de_horas_trabalhadas = float(input("Digite o número de horas trabalhadas"))

salario_bruto = valor_da_hora_trabalhada * numero_de_horas_trabalhadas

print("Seu salário bruto será de: R$",salario_bruto)
