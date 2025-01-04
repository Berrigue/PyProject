#Dicionarios

elemento = {
    'z':3, 'nome': 'Lítio', 'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento:{elemento['nome']} ')
print(f'Densidade:{elemento['densidade']} ')
print(f'o dicionario possui {len(elemento)} elementos.')

#atualizar uma entrada do dicionario

elemento['grupo'] = 'Alcalinos'
print(elemento)

#adicionar uma entrada no dicionario

elemento['período'] = 1
print(elemento)

#exclusao de itens em dicionario
# del elemento['período']
# print(elemento)

# elemento.clear()
# print(elemento)

# del elemento
# print(elemento)

#visualizar os elementos do dicionario

print(elemento.items())
for i in elemento.items():
    print(i)


print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f'{i}: {j}')