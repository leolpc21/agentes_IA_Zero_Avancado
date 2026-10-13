"""Exercícios de fundamentos em Python.

Este arquivo reúne atividades práticas para revisar e reforçar os conteúdos
estudados em fundamentos de Python, como:
- variáveis e tipos de dados
- operadores
- strings
- listas, tuplas e sets
- dicionários
- condicionais
- laços de repetição
- list comprehension
- funções
- *args e **kwargs
- funções lambda

Instruções:
1. Leia cada exercício antes de responder.
2. Tente resolver sozinho antes de consultar a solução.
3. Teste cada função com entradas diferentes.
4. Ao terminar, faça melhorias e tente criar variações dos exercícios.
5. Os exemplos de retorno abaixo são apenas ilustrativos.
   Eles ajudam a entender o formato esperado, mas não são a única resposta correta.
"""


# ---------------------------------------------------------------------------
# Exercício 1: Tipos de dados e operadores
# ---------------------------------------------------------------------------
# Objetivo:
# Receber dois números e calcular as operações básicas.
#
# Crie uma função chamada calcular_operacoes(num1, num2) que:
# - some os números
# - subtraia os números
# - multiplique os números
# - divida os números
# - calcule o resto da divisão
# - retorne tudo em um dicionário
#
# Exemplo de uso:
# calcular_operacoes(10, 5)
#
# Exemplo de retorno (ilustrativo, apenas para orientar o formato):
# {'soma': 15, 'subtracao': 5, 'multiplicacao': 50, 'divisao': 2.0, 'resto': 0}


def calcular_operacoes(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2

    if num2 == 0:
        divisao = None
        resto = None
    else:
        divisao = num1 / num2
        resto = num1 % num2

    return {
        "soma": soma,
        "subtracao": subtracao,
        "multiplicacao": multiplicacao,
        "divisao": divisao,
        "resto": resto,
    }


print(calcular_operacoes(10, 5))
print(calcular_operacoes(0, 5))
print(calcular_operacoes(10, 0))
print(calcular_operacoes(5, 10))


# ---------------------------------------------------------------------------
# Exercício 2: Conversão de dados
# ---------------------------------------------------------------------------
# Objetivo:
# Ler dados do usuário e formatar uma mensagem final.
#
# Peça ao usuário para informar:
# - nome
# - idade
# - altura
#
# Converta a idade para inteiro e a altura para float.
# Depois, exiba uma mensagem formatada como:
# "Nome: X | Idade: Y anos | Altura: Z metros"
#
# Exemplo de uso:
# dados_usuario()
#
# Exemplo de retorno (ilustrativo):
# "Nome: Maria | Idade: 20 anos | Altura: 1.68 metros"


def dados_usuario():
    nome = input("Digite um nome:\n").strip()
    idade_texto = input("Digite a sua idade: ").strip()
    altura_texto = input("Digite sua altura: ").strip().replace(",", ".")

    if not nome:
        nome = "Usuário"

    while not idade_texto.isdigit():
        print("Idade inválida. Digite apenas números válidos.")
        idade_texto = input("Digite a sua idade: ").strip()
    idade = int(idade_texto)

    while True:
        try:
            altura = float(altura_texto)
            if altura <= 0:
                raise ValueError
            break
        except ValueError:
            print("Altura inválida. Digite um número válido.")
            altura_texto = input("Digite sua altura: ").strip().replace(",", ".")

    return f"Nome: {nome} | Idade: {idade} anos | Altura: {altura} metros"


print(dados_usuario())

# ---------------------------------------------------------------------------
# Exercício 3: Condicionais
# ---------------------------------------------------------------------------
# Objetivo:
# Verificar se a pessoa é maior de idade.
#
# Crie uma função chamada verificar_maior_idade(idade) que:
# - retorne "Menor de idade" se idade < 18
# - retorne "Maior de idade" se idade >= 18
# - retorne "Idade inválida" se idade for negativa
#
# Exemplo de uso:
# verificar_maior_idade(20)
#
# Exemplo de retorno (ilustrativo):
# "Maior de idade"


def verificar_maior_idade(idade):
    try:
        idade = int(idade)
        if idade < 0:
            return f"{idade} - Idade inválida"
        elif idade < 18:
            return f"{idade} - Menor de idade"
        elif idade >= 18:
            return f"{idade} - Maior de idade"
    except ValueError:
        return f"{idade} - Valor inválido"


print(verificar_maior_idade("dez"))
print(verificar_maior_idade(-10))
print(verificar_maior_idade(0))
print(verificar_maior_idade(10))
print(verificar_maior_idade(17.5))
print(verificar_maior_idade(18))
print(verificar_maior_idade(20))
print(verificar_maior_idade("25"))


# ---------------------------------------------------------------------------
# Exercício 4: Comparações e decisões compostas
# ---------------------------------------------------------------------------
# Objetivo:
# Classificar uma nota com base em faixas de avaliação.
#
# Crie uma função chamada avaliar_nota(nota) que:
# - se nota >= 90: "Excelente"
# - se nota >= 70: "Bom"
# - se nota >= 50: "Regular"
# - caso contrário: "Insuficiente"
#
# Teste com valores diferentes.
#
# Exemplo de uso:
# avaliar_nota(85)
#
# Exemplo de retorno (ilustrativo):
# "Bom"


def avaliar_nota(nota):
    try:
        nota_str = str(nota).replace(",", ".")
        nota = float(nota_str)
        if nota < 0:
            return "Nota inválida"
        elif nota >= 90:
            return "Excelente"
        elif nota >= 70:
            return "Bom"
        elif nota >= 50:
            return "Regular"
        else:
            return "Insuficiente"
    except ValueError:
        return "Nota inválida"


print(avaliar_nota("dez"))
print(avaliar_nota(-49))
print(avaliar_nota(0))
print(avaliar_nota(49.5))
print(avaliar_nota(50))
print(avaliar_nota(50.6))
print(avaliar_nota(65))
print(avaliar_nota(69))
print(avaliar_nota(70))
print(avaliar_nota(75))
print(avaliar_nota(89))
print(avaliar_nota(90))
print(avaliar_nota(95))
print(avaliar_nota("100"))
print(avaliar_nota("75.9"))
print(avaliar_nota("75,9"))


# ---------------------------------------------------------------------------
# Exercício 5: Strings
# ---------------------------------------------------------------------------
# Objetivo:
# Tratar textos e padronizar o nome.
#
# Crie uma função chamada formatar_nome(nome) que:
# - remova espaços extras no início e no fim
# - transforme para letras minúsculas ou maiúsculas
# - imprima o nome formatado em um texto amigável
#
# Exemplo: "  maria da silva  " -> "Maria da Silva"
#
# Exemplo de uso:
# formatar_nome("  maria da silva  ")
#
# Exemplo de retorno (ilustrativo):
# "Nome formatado: Maria da Silva"


def formatar_nome(nome):
    if nome is None or not isinstance(nome, str):
        return "Nome inválido"

    nome = nome.title().strip()
    nome = " ".join(nome.split())

    if not nome:
        return "Nome vazio"

    return f"Nome formatado: {nome}"


print(formatar_nome(" leo costa "))
print(formatar_nome("leo costa "))
print(formatar_nome(" leo costa"))
print(formatar_nome("  leo da costa  "))
print(formatar_nome("   leo  da  silva   "))
print(formatar_nome(12345))
print(formatar_nome(None))
print(formatar_nome(""))
print(formatar_nome(" "))


# ---------------------------------------------------------------------------
# Exercício 6: Listas
# ---------------------------------------------------------------------------
# Objetivo:
# Manipular itens em uma lista.
#
# Crie uma função chamada adicionar_item(lista, item) que:
# - adicione o item à lista
# - retorne a lista tualizada
#
# Depois, crie uma segunda função chamada remover_item(lista, item) que:
# - remova o item da lista
# - retorne a lista atualizada
#
# Exemplo de uso:
# adicionar_item([1, 2, 3], 4)
# remover_item([1, 2, 3, 4], 3)
#
# Exemplo de retorno (ilustrativo):
# [1, 2, 3, 4]
# [1, 2, 4]

lista = [1, 2, 3]


def validar_lista(lista):
    return isinstance(lista, list)


def item_eh_nulo(item):
    return item is None


def adicionar_item(lista, item=None):
    if not validar_lista(lista):
        return "Erro: O primeiro argumento não é uma lista"

    if item_eh_nulo(item):
        return "Erro: O segundo argumento (item) é obrigatório"

    if item in lista:
        return f"Erro: O item '{item}' já está na lista"

    lista.append(item)
    return lista


def remover_item(lista, item=None):
    if not validar_lista(lista):
        return "Erro: O primeiro argumento não é uma lista"

    if item_eh_nulo(item):
        return "Erro: O segundo argumento (item) é obrigatório"

    if len(lista) == 0:
        return "Erro: A lista está vazia"

    if item not in lista:
        return "Erro: Item não está presente na lista"

    lista.remove(item)
    return lista


print(adicionar_item(lista, 4))
print(remover_item(lista, 3))
print(adicionar_item([], 1))

print(adicionar_item(lista, 4))
print(adicionar_item({1, 2, 3}, 4))
print(adicionar_item(None, 4))
print(adicionar_item(lista))

print(remover_item({1, 2, 3}, 4))
print(remover_item(None, 4))
print(remover_item(lista))
print(remover_item([], 4))
print(remover_item(lista, 6))


# ---------------------------------------------------------------------------
# Exercício 7: Tuplas e listas
# ---------------------------------------------------------------------------
# Objetivo:
# Trabalhar com dados imutáveis e depois convertê-los em lista.
#
# Crie uma tupla com os dias da semana e imprima:
# - o primeiro dia
# - o último dia
# - o tamanho da tupla
#
# Em seguida, converta essa tupla para lista e adicione um novo dia.
#
# Exemplo de uso:
# manipular_dias_semana()
#
# Exemplo de retorno (ilustrativo):
# Primeiro dia: Domingo
# Último dia: Sábado
# Tamanho: 7
# Lista final: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Feriado']

dias_da_semana = (
    "Domingo ",
    " Segunda",
    " Terça ",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado",
)


def limpar_espaco_extra_lista(lista):
    return [dia.strip().title() for dia in lista]


def manipular_dias_semana(semana, novo_dia=None):
    if not isinstance(semana, tuple):
        return {"sucesso": False, "erro": "O parâmetro 'semana' não é uma tupla."}

    if len(semana) == 0:
        return {"sucesso": False, "erro": "O parâmetro 'semana' está vazio."}

    if novo_dia is None or not isinstance(novo_dia, str):
        return {
            "sucesso": False,
            "erro": f"O parâmetro 'novo_dia' - {novo_dia} é inválido.",
        }

    novo_dia = novo_dia.strip().title()

    if not novo_dia:
        return {
            "sucesso": False,
            "erro": "O parâmetro 'novo_dia' é uma string vazia.",
        }

    lista_semana = limpar_espaco_extra_lista(list(semana))

    if any(novo_dia.casefold() == dia.casefold() for dia in lista_semana):
        return {
            "sucesso": False,
            "erro": f"O item '{novo_dia}' já está na lista.",
        }

    primeiro_dia = lista_semana[0]
    ultimo_dia = lista_semana[-1]
    tamanho_original = len(lista_semana)
    lista_semana.append(novo_dia)

    return {
        "sucesso": True,
        "primeiro_dia": primeiro_dia,
        "ultimo_dia": ultimo_dia,
        "tamanho": tamanho_original,
        "lista_final": lista_semana,
    }


resultado = manipular_dias_semana(dias_da_semana, " Feriado ")

print(f"Primeiro dia: {resultado['primeiro_dia']}")
print(f"Último dia: {resultado['ultimo_dia']}")
print(f"Tamanho da lista: {resultado['tamanho']}")
print(f"Lista final: {resultado['lista_final']}")
print(manipular_dias_semana(dias_da_semana, " Feriado "))
print(manipular_dias_semana(["Domingo"], "Feriado"))
print(manipular_dias_semana((), "Feriado"))
print(manipular_dias_semana(dias_da_semana))
print(manipular_dias_semana(dias_da_semana, 1234))
print(manipular_dias_semana(dias_da_semana, "Sábado"))
print(manipular_dias_semana(dias_da_semana, "sábado"))
print(manipular_dias_semana(dias_da_semana, ""))
print(manipular_dias_semana(dias_da_semana, " "))


# ---------------------------------------------------------------------------
# Exercício 8: Sets
# ---------------------------------------------------------------------------
# Objetivo:
# Encontrar elementos repetidos e exclusivos usando conjuntos.
#
# Crie duas listas com nomes de alunos e descubra:
# - alunos repetidos nas duas turmas
# - alunos exclusivos de cada turma
# - o total de alunos distintos
#
# Use set para resolver.
#
# Exemplo de uso:
# comparar_turmas(['Ana', 'Bruno', 'Carla'], ['Bruno', 'Duda', 'Ana'])
#
# Exemplo de retorno (ilustrativo):
# {'Ana', 'Bruno'}
# {'Carla'}
# {'Ana', 'Bruno', 'Carla', 'Duda'}


def comparar_turmas(turma_a, turma_b):
    # TODO: implemente a lógica
    pass


# ---------------------------------------------------------------------------
# Exercício 9: Dicionários
# ---------------------------------------------------------------------------
# Objetivo:
# Organizar informações em um dicionário e calcular a média.
#
# Crie um dicionário com dados de um aluno:
# {
#     "nome": "Ana",
#     "idade": 20,
#     "curso": "Python",
#     "notas": [8.5, 9.0, 7.5]
# }
#
# Crie uma função chamada resumo_aluno(aluno) que:
# - mostre o nome, idade e curso
# - calcule a média das notas
# - retorne uma frase com a média final
#
# Exemplo de uso:
# resumo_aluno({"nome": "Ana", "idade": 20, "curso": "Python", "notas": [8.5, 9.0, 7.5]})
#
# Exemplo de retorno (ilustrativo):
# "Ana, 20 anos, cursando Python. Média final: 8.33"


def resumo_aluno(aluno):
    # TODO: implemente a lógica
    pass


# ---------------------------------------------------------------------------
# Exercício 10: Loops
# ---------------------------------------------------------------------------
# Objetivo:
# Filtrar números pares usando laços.
#
# Crie uma função chamada listar_pares(inicio, fim) que:
# - percorra os números entre inicio e fim
# - retorne uma lista apenas com os números pares
#
# Faça também uma versão usando while.
#
# Exemplo de uso:
# listar_pares(1, 10)
#
# Exemplo de retorno (ilustrativo):
# [2, 4, 6, 8, 10]


def listar_pares(inicio, fim):
    # TODO: implemente a lógica com for
    pass


def listar_pares_while(inicio, fim):
    # TODO: implemente a lógica com while
    pass


# ---------------------------------------------------------------------------
# Exercício 11: List Comprehension
# ---------------------------------------------------------------------------
# Objetivo:
# Criar listas compactas com expressão lógica.
#
# Crie uma função chamada quadrados_pares(numero_final) que:
# - retorne os quadrados dos números pares de 1 até numero_final
#
# Exemplo: numero_final = 10 -> [4, 16, 36, 64, 100]
#
# Exemplo de uso:
# quadrados_pares(10)
#
# Exemplo de retorno (ilustrativo):
# [4, 16, 36, 64, 100]


def quadrados_pares(numero_final):
    # TODO: implemente a lógica com list comprehension
    pass


# ---------------------------------------------------------------------------
# Exercício 12: Funções
# ---------------------------------------------------------------------------
# Objetivo:
# Calcular a média de uma sequência numérica.
#
# Crie uma função chamada calcular_media(notas) que:
# - receba uma lista de notas
# - calcule a média aritmética
# - retorne a média
#
# Se a lista estiver vazia, retorne 0.
#
# Exemplo de uso:
# calcular_media([7, 8, 9, 10])
#
# Exemplo de retorno (ilustrativo):
# 8.5


def calcular_media(notas):
    # TODO: implemente a lógica
    pass


# ---------------------------------------------------------------------------
# Exercício 13: *args e **kwargs
# ---------------------------------------------------------------------------
# Objetivo:
# Entender como receber quantidade variável de argumentos.
#
# Crie uma função chamada mostrar_dados(*args, **kwargs) que:
# - imprima os valores recebidos em args
# - imprima os pares chave-valor de kwargs
#
# Exemplo de uso:
# mostrar_dados("Python", "Java", curso="Python", nivel="iniciante")
#
# Exemplo de retorno (ilustrativo):
# Python
# Java
# curso -> Python
# nivel -> iniciante


def mostrar_dados(*args, **kwargs):
    # TODO: implemente a lógica
    pass


# ---------------------------------------------------------------------------
# Exercício 14: Funções lambda
# ---------------------------------------------------------------------------
# Objetivo:
# Entender funções anônimas e uso prático em expressões simples.
#
# Crie 3 lambdas para:
# 1. dobrar um número
# 2. verificar se um número é par
# 3. concatenar "Olá, " + nome
#
# Depois teste cada uma em exemplos.
#
# Exemplo de uso:
# dobrar(5)
# eh_par(8)
# saudar("Maria")
#
# Exemplo de retorno (ilustrativo):
# 10
# True
# "Olá, Maria"


dobrar = lambda numero: numero * 2
# TODO: criar as outras lambdas


def exercicio_lambda():
    # TODO: teste as lambda aqui
    pass


# ---------------------------------------------------------------------------
# Desafio 1: Calculadora com menu
# ---------------------------------------------------------------------------
# Objetivo:
# Criar uma calculadora simples com entrada do usuário.
#
# Crie um programa que pergunte ao usuário:
# - primeiro número
# - segundo número
# - operação (+, -, *, /)
#
# O programa deve calcular e mostrar o resultado.
# Trate a divisão por zero com mensagem amigável.
#
# Exemplo de uso:
# calculadora_menu()
#
# Exemplo de retorno (ilustrativo):
# Resultado: 15.0
# ou
# Não é possível dividir por zero.


def calculadora_menu():
    # TODO: implemente a calculadora com menu
    pass


# ---------------------------------------------------------------------------
# Desafio 2: Cadastro de alunos
# ---------------------------------------------------------------------------
# Objetivo:
# Organizar dados em lista de dicionários e fazer consultas.
#
# Crie uma lista de dicionários com alunos.
# Cada aluno deve ter:
# nome, idade, curso
#
# Depois:
# - mostre todos os alunos
# - filtre por curso
# - calcule a média de idade
#
# Exemplo de uso:
# cadastro_de_alunos()
#
# Exemplo de retorno (ilustrativo):
# [{'nome': 'Ana', 'idade': 20, 'curso': 'Python'}, {'nome': 'Pedro', 'idade': 22, 'curso': 'Python'}]
# Média de idade: 21.0


def cadastro_de_alunos():
    # TODO: implemente a lógica
    pass


# ---------------------------------------------------------------------------
# Desafio 3: Analisador de texto
# ---------------------------------------------------------------------------
# Objetivo:
# Explorar manipulação de strings e listas.
#
# Receba uma frase do usuário e:
# - conte quantas letras existem
# - conte quantos espaços existem
# - converta para maiúsculas
# - separe as palavras em uma lista
#
# Use string, listas e laços de repetição.
#
# Exemplo de uso:
# analisador_texto("Python para iniciantes")
#
# Exemplo de retorno (ilustrativo):
# Letras: 22
# Espaços: 3
# Texto em maiúsculas: PYTHON PARA INICIANTES
# Palavras: ['Python', 'para', 'iniciantes']


def analisador_texto(frase):
    # TODO: implemente a lógica
    pass
