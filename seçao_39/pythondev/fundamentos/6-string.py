# Case sensitive

movieName = "The Matrix"
print(movieName) 

movieName2 = "the matrix"
print(movieName2)

print(f"Os nomes são iguais? {movieName == movieName2}") # False


# String Multilinhas
movieDescription = '''
  This is a description of the movie.
  It can be multiple lines.
  It can also contain special characters like "quotes" and 'single quotes'.
'''
print(movieDescription)

# Multiplicação de strings

line = "="
print(line * 20) # imprime 20 vezes o caractere "="

# Procurar uma palavra dentro de uma string

print(f"O nome do filme contém 'matrix'? {'matrix' in movieName}") # False
print(f"O nome do filme contém 'Matrix'? {'Matrix' in movieName}") # True