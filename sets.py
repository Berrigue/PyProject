# Set são coleções de elementos únicos que não são ordenados.

# planeta_anao = {'Plutão', 'Cere', 'Eris', 'Haumea', 'Makemake'}
# print(planeta_anao)

# print(len(planeta_anao))
#print('Lua' not in planeta_anao) 

#for astro in planeta_anao:
#   print(astro.upper())

# astros = ['Lua','Vênus', 'Sirius', 'Marte', 'Lua']
# print(astros)

# astros_set = set(astros)
# print(astros_set)

astros1 = {'Lua','Vênus', 'Sirius', 'Marte'}
astros2 = {'Lua','Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}

print(astros1 | astros2)
print(astros1.union(astros2))

print(astros1 & astros2)
print(astros1.intersection(astros2))

print(astros1.symmetric_difference(astros2))

#add items

astros1.add('Urano')
astros1.add('Sol')

print(astros1)

astros1.remove('Sirius')

# Remove algum item de forma aleatoria
astros1.pop()

print(astros1)