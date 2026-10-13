"""
1- Escreva um programa que lê dois nomes e retorne uma string formatada no formato "UltimoNome, PrimeiroNome".
2- Inverta a ordem das palavras em uma string fornecida.
3- Verifique se uma string fornecida é um palíndromo (pode ser lida da mesma forma de trás para frente).

"""
# 1

primeiroNome = input("Digite o primeiro nome: \n")
ultimoNome = input("Digite o último nome: \n")

print(f"{ultimoNome}, {primeiroNome}")

# 2

frase = input("Digite uma frase: \n")
palavras = frase.split()
fraseInvertida = ' '.join(palavras[::-1])
print(f"Frase invertida: {fraseInvertida}")

# 3

texto1 = "arara"
texto2 = "python"

# Remover espaços em branco e converter para minúsculas
texto_formatado1 = texto1.lower().replace(" ", "")
texto_formatado2 = texto2.lower().replace(" ", "")

# Verificar se são palíndromos
if texto_formatado1 == texto_formatado1[::-1]:
    print(f"'{texto1}' é um palíndromo.")
else:
    print(f"'{texto1}' não é um palíndromo.")

if texto_formatado2 == texto_formatado2[::-1]:
    print(f"'{texto2}' é um palíndromo.")
else:
    print(f"'{texto2}' não é um palíndromo.")