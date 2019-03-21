# Tipos de Dados

# Tipo de dado (nomenclatura do Python)

# Inteiros (int)
# Números inteiros, sejam positivos ou não.

int1 = 3
int2 = 42

# Suporta operações como multiplicação e soma.

# Reais (float)
# Números Reais

fl1 = 3.14
fl2 = 6.9

# Suporta operações como multiplicação e soma.


# Strings (str)
# Cadeia de caractéres.
# A ordem importa.
# Podem ser aspas simples ou duplas.
# Caractér de escape: "\n"

s1 = "Olá mundo1."
s2 = 'Oi mundo1, fala comigo.'

# Manuseando strings
# Podemos acessar elementos da string (caractéres) com os índices.
s1[0]
# Retorna 'O'
s2[-1]
# Retorna '.'
s2[2]
# Retorna ' '
s2.upper()          # Retornar a string toda em maiúscula
s1.lower()          # Retornar a string toda em minúscula
s1.isascii()        # Retorna True se a string for toda códigos ASCII     


# Boolean (bool)
# Testes de condições

bool1 = True
bool2 = False

# Trabalhando com booleans (Algebra booleana)

(True and True)
# Retorna True
(True and False)
# Retorna False
(True or False)
# Retorna True
(False or True)
# Retorna True


# Listas (list)
# Conjunto mutável de objetos.
# A ordem importa.

list1 = [42, int2, "Olá mundo2.", bool1]
list2 = []

list1[0]    # Retorna o primeiro item da lista
# Retorna 42
list1[3]    # Retorna o quarto item da lista
# Retorna bool1
list1[-1]    # Retorna último item da lista
# Retorna bool1
list1[-3]    # Retorna o antepenúltimo item da lista
# Retorna int2

# Manuseando listas:
list1.append("42")   # Adiciona um item ao final da lista
list1.pop(-1)        # Retorna e remove o último item
list1.reverse()      # Inverte a lista
list1[0] = 44
# Altera o item list1[0] (42) para 44

# Slicing de lista
# Recorte de uma lista onde o primeiro índice é intervalo fechado e o último, aberto.
list1[0:2] # Igual a list1[:2]
# Retorna [42, int2]
list1[1:]
# Retorna [int2, "Olá mundo2.", bool1]

# Tuplas (tuple)
# Conjunto imutável de objetos.
# A ordem importa.
# Também suporta slicing.

t1 = (4.6, 5.0)
t2 = ('André', 'Pitas')

# Acessamos o conteúdo das tuplas da mesma maneira que acessamos listas ou strings
t1[0] 
# Retorna 4.6


# Dicionários (dic)
# Conjunto de elementos identificados por um valor chave.

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e
# Retorna True

d1 = {'inerte': "Algo que não se move por conta própria", 'dole': "gay" }
d['dole']
# Retorna 'gay'# Retornar a string toda em maiúscula

# Acessando valores de um dicionário
a['one']
# Retorna 1