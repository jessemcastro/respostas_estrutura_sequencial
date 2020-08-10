#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

temperatura_C = float(input("Digite a temperatura em Cº"))
temperatura_F = temperatura_C * 1.8 + 32
temperatura_F_arredondada = temperatura_F//1

print("A temperatura em Cº é aproximadamente ",temperatura_F_arredondada)