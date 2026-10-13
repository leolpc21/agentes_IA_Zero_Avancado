
# Fatorial de um número
"""
Fatorial de um numero:
1 -> 1 = 1
2 -> 2 * 1 = 2
3 -> 3 * 2 * 1 = 6
4 -> 4 * 3 * 2 * 1 = 24
5 -> 5 * 4 * 3 * 2 * 1 = 120
"""

def factorial(num):
  if num == 1:
    return 1
  else:
    return (num * factorial(num - 1))

print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(3)) # 6
print(factorial(4)) # 24
print(factorial(5)) # 120

"""
Como funciona a lógica do código:
- Caso Base (if num == 1): É o ponto de parada para evitar um loop infinito. Quando o número chega a 1, a função para de chamar a si mesma e retorna 1.
- Caso Recursivo (else): Multiplica o número atual pelo fatorial do número anterior (num - 1), empilhando as chamadas até chegar ao caso base.

Exemplo Prático: Executando factorial(4)
Quando você executa factorial(4), o Python resolve em duas fases: Empilhamento (indo até o fim) e Desempilhamento (resolvendo as contas na volta).

1ª Fase: Empilhamento (Chamadas das funções)
- factorial(4): Não é 1, então executa 4 * factorial(3) (aguarda o resultado de factorial(3))
- factorial(3): Não é 1, então executa 3 * factorial(2) (aguarda o resultado de factorial(2))
- factorial(2): Não é 1, então executa 2 * factorial(1) (aguarda o resultado de factorial(1))
- factorial(1): Atinge o caso base (num == 1) e retorna 1.

2ª Fase: Desempilhamento (Resolvendo os retornos)
Agora que a última chamada retornou 1, o Python resolve as contas de trás para frente:
- factorial(2) recebe 1 e calcula: 2 * 1 = 2
- factorial(3) recebe 2 e calcula: 3 * 2 = 6
- factorial(4) recebe 6 e calcula: 4 * 6 = 24

Resultado final retornado: 24.

Resumo Visual factorial(4) = 4 * (3 * (2 * 1)) = 24
"""

number = int(input("Digite o número para o fatorial:\n"))
print(f"O fatorial de '{number}' é: {factorial(number)}")

# Soma total de um número

def total_sum(num):
  if num == 1:
    return 1
  else:
    return (num + total_sum(num-1))

num = int(input("Digite o número para a soma total:\n"))
print(f"A soma total do '{num}' é: {total_sum(num)}")

print(total_sum(1))
print(total_sum(2))
print(total_sum(3))
print(total_sum(4))
print(total_sum(5))

"""
Soma total de um numero:
1 -> 1 = 1
2 -> 2 + 1 = 3
3 -> 3 + 2 + 1 = 6
4 -> 4 + 3 + 2 + 1 = 10
5 -> 5 + 4 + 3 + 2 + 1 = 15
"""