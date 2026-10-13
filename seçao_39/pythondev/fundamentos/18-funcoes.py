
# Função para imprimir uma mensagem
  # def: Indica ao Python que você está criando uma função.

def welcome():
  print("Bem vindo ao sistema de filmes!")

welcome()

# Função para calcular a média de notas

def calculate_average():
  num_ratings = int(input(" Digite quantas avaliações deseja fazer pro filme:\n"))
  total = 0
  for i in range(num_ratings):
    note = float(input("Digite a nota para o filme:\n"))
    total += note

  if (num_ratings > 0):
    average = total / num_ratings
  else:
    average = 0

  return average

print(f"A média de avaliações é: {calculate_average():.2f}")

# Função para cadastrar um filme

def create_movie():
  name = input("Digite o nome do filme: \n")
  year_launch = int(input("Digite o ano de lançamento do filme: \n"))
  movie_price = float(input("Digite o preço do filme: \n"))
  rating = float(input("Digite a nota do filme: \n"))

  print(f"{name} ({year_launch}-{rating}) - R${movie_price:.2f}")

create_movie()
