
# Função para imprimir um nome completo

def full_name(first_name, last_name):
  print(f"Nome é: {first_name} {last_name}")

full_name("Leo", 'Costa')

# Função para somar dois numeros

def sum_numbers(a, b):
  return a + b

print(f"Soma é: {sum_numbers(10,20)}")

# Função com parametros default

def address(country="Brasil"):
  print(f"Eu moro em: {country}")

address()
address("Portugal")

# Função para avaliar filme

def rate_movie(num_ratings, movie_name):
  total = 0
  for i in range(num_ratings):
    note = float(input("Digite a nota do filme:\n"))
    total += note

  if num_ratings > 0:
    average = total / num_ratings
  else:
    average = 0

  return print(f"Média de avaliação do filme: {movie_name} é: {average:.2f}")

rate_movie(2, "Mario")