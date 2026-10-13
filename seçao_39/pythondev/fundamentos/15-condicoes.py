# Informações sobre o filme

name = input("Digite o nome do filme: \n")
year = int(input("Digite o ano de lançamento: \n"))
rating = float(input("Digite a nota de avaliação do filme (0.0 a 10.0): \n"))

# Verifica se o filme é recomendado com base na nota de avaliação
if rating > 8 and year > 2015:
    print(f"O filme '{name}' lançado em {year} é recomendado.")
else:
    print(f"O filme '{name}' lançado em {year} não é recomendado.")

# Calculadora simples
num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
operation = input("Digite a operação desejada (+, -, *, /): \n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":  
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        result = 0
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")
    result = 0

print(f"Resultado da operação é: {result:.2f}")