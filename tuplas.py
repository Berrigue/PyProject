#tuplas são imutaveis

halogenios = ('F','Cl','Br','I','At',)
gases_nobres = ('He','Ne','Ar','Xe')

elementos_novos = halogenios + gases_nobres

print(elementos_novos)

# tupla = (1,2,3,4,5)
# print(tupla)

# Operaçoes não disponiveis em tuplas: .sort(), .append(), .reverse(), .pop()...
# como a tupla é IMUTAVEL quaisquer altercoes dentro da lista são indisponiveis.


#convertendo uma lista para uma tupla
lista = ['teste', 'teste2', 'teste3']

lista2 = tuple(lista)

print(type(lista2))

