movieName = "The Matrix"
print(movieName) 

# string[inicio:fim] - indice começa na posição 0 / indice final -1

# Buscar toda string a partir da primeira posição
print(movieName[0:]) # The Matrix

# Buscar toda string até a ultima posição
print(movieName[:10]) # The Matrix

# Buscar toda string a partir da terceira até a ultima posição
print(movieName[2:10]) # e Matrix

# string[inicio:fim:passo] - passo é o tamanho do salto entre os caracteres
"""
indice começa na posição 0 / indice final -1
passo - determina o incremento. Por padrão esse número é o 1, ou seja, ele vai percorrer a string caractere por caractere. Se você colocar 2, ele vai pular de 2 em 2, e assim por diante.
"""

# Buscar toda a string de 2 em 2 caracteres
print(movieName[::2]) # TeMti

# Buscar toda a string nos indices impares
print(movieName[1::2]) # h arx

# Inverter uma string de trás para frente
print(movieName[::-1]) # xirtaM ehT