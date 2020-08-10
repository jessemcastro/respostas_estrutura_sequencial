#Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

temperatura_F = float(input("Digite a temperatura em Fº"))
temperatura_C = 5*((temperatura_F-32)/9)
temperatura_C_arredondada = temperatura_C//1

print("A temperatura em Cº é aproximadamente ",temperatura_C_arredondada)