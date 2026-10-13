# Comando para receber um valor de entrada - Input

# Funções de Conversão de Tipos de Dados
"""
int() # Converte para inteiro
float() # Converte para decimal
str() # Converte para string
"""

name = input("Digite o nome do filme: \n")
year_launch = int(input("Digite o ano de lançamento do filme: \n"))
note_movie = float(input("Digite a nota do filme: \n"))
planIncluded = (
    input("Digite se o filme está incluso no plano (True/False): \n").strip().lower()
    == "true"
)

print(f"O nome do filme é: {name}!")
print(f"O ano de lançamento do filme é: {year_launch}!")
print(f"A nota do filme é: {note_movie}!")
print(f"O filme está incluso no plano? {planIncluded}!")

print(type(name))  # <class 'str'> string
print(type(year_launch))  # <class 'int'> integer
print(type(note_movie))  # <class 'float'> float
print(type(planIncluded))  # <class 'bool'> boolean


"""
Para que serve o 'f' dentro do print? 

Ele serve para formatar a string, permitindo a inclusão de variáveis dentro da string usando chaves {}. No exemplo acima, a variável 'name' é inserida na string formatada, resultando em uma saída personalizada com o valor digitado pelo usuário.
"""

"""
Input sempre retornará uma string, mesmo que o usuário digite um número. Se você quiser armazenar o valor como um tipo diferente (como int ou float), será necessário converter a entrada usando funções como int() ou float().
"""
