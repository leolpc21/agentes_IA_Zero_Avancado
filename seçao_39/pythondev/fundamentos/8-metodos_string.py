movieName = " The Matrix "

movieDescription = """
  This is a description of the movie.
  It can be multiple lines.
  It can also contain special characters like "quotes" and 'single quotes'.
"""
palavras = ["Jutando", "as", "palavras", "da", "string"]

print(f"'{movieName.upper()}'")  # ' THE MATRIX ' - Tudo em maiúsculo
print(f"'{movieName.lower()}'")  # ' the matrix ' - Tudo em minúsculo
print(
    f"'{movieName.capitalize()}'"
)  # ' The matrix ' - Primeira letra da primeira palavra em maiúsculo
print(
    f"'{movieName.title()}'"
)  # ' The Matrix ' - Primeira letra de cada palavra em maiúsculo
print(
    f"'{movieName.center(15, '-')}'"
)  # '-- The Matrix -' - Centraliza a string e preenche com o caractere especificado. O preenchimento acontece nos dois lados da string, até que a largura total seja atingida. Se a largura total for menor que o tamanho da string, a string será retornada sem alterações.
print(
    f"'{movieName.strip()}'"
)  # 'The Matrix' - Remove espaços em branco no início e no final da string
print(
    f"'{movieName.find('Matrix')}'"
)  # '5' - Retorna o índice da primeira ocorrência da substring especificada. Se a substring não for encontrada, retorna -1.
print(
    f"'{movieName.count('a')}'"
)  # '1' - Retorna o número de ocorrências da substring especificada.
print(
    f"'{movieName.replace('Matrix', 'Matrix Reloaded')}'"
)  # ' The Matrix Reloaded ' - Retorna uma nova string com todas as ocorrências da substring especificada substituídas pela nova substring. A string original não é alterada.
print(
    f"'{movieDescription.split('can')}'"
)  # '['\n  This is a description of the movie.\n  It ', ' be multiple lines.\n  It ', ' also contain special characters like "quotes" and \'single quotes\'.\n']' - Retorna uma lista de substrings, dividindo a string original na substring especificada. A substring especificada é removida da lista resultante. Se a substring não for encontrada, a lista conterá apenas a string original.
print(
    f"'{movieName.startswith('The')}'"
)  # 'True' - Retorna True se a string começar com a substring especificada, caso contrário, retorna False.
print(
    f"'{movieName.endswith('Matrix')}'"
)  # 'True' - Retorna True se a string terminar com a substring especificada, caso contrário, retorna False.
print(
    f"'{movieName.isnumeric()}'"
)  # 'False' - Retorna True se todos os caracteres da string forem numéricos, caso contrário, retorna False.
print(
    f"'{' '.join(palavras)}'"
)  # 'Jutando as palavras da string' - Retorna uma nova string, concatenando os elementos de uma lista de strings, separados pela substring especificada. A string original não é alterada.
print(
    f"'{' '.join(movieName.split()[::-1])}'"
)  # 'Matrix The' - Retorna uma nova string com as palavras da string original invertidas. A string original não é alterada. A função split() divide a string em uma lista de palavras, e a função join() junta as palavras da lista em uma nova string, separadas por um espaço. O operador [::-1] inverte a ordem da lista de palavras.

"""
Diferença entre .isdigit() e .isnumeric()
Ambos são métodos da classe str (texto) que verificam se uma string contém apenas caracteres numéricos e retornam um valor booleano (True ou False). A diferença está no escopo e no tipo de caracteres aceitos por cada uma:

.isdigit() (Dígitos):
  Verifica se todos os caracteres da string são dígitos. Além dos números tradicionais de 0 a 9, ele aceita caracteres que representam dígitos sobrescritos e subscritos (como ² ou ³).
  Exemplo: "123".isdigit() -> True
  Exemplo: "²".isdigit() -> True
  Exemplo: "½".isdigit() -> False

.isnumeric() (Numérico amplo):
  É uma função mais abrangente. Ela engloba tudo o que o .isdigit() aceita, além de incluir qualquer caractere Unicode que represente um conceito numérico, como frações (ex: ½, ¾), numerais romanos, caracteres numéricos de outros idiomas (como chinês ou árabe) e numerais circulados.
  Exemplo: "123".isnumeric() -> True
  Exemplo: "²".isnumeric() -> True
  Exemplo: "½".isnumeric() -> True
"""

"""
Exercício 5 - Operações em Strings

Escreva um programa que leia uma palavra e um número inteiro n.
O programa deve:
- Imprimir a palavra duas vezes concatenada (sem espaço).
- Imprimir a palavra repetida n vezes (usando multiplicação de string).

Exemplo
Entrada:
Python
3

Saída:
PythonPython
PythonPythonPython
"""

s = "Python"
n = 3

print(s * 2)
print(s * n)
