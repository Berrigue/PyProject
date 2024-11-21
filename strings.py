#manipulações de strings em python
#strings são imutaveis, mas você consegue alterar o valor de uma variavel que contem a string

# frase = 'Vamos aprender python hoje.'
# palavras = frase.split()

# print(palavras[1])

# for palavra in palavras:
#     print(palavra)

# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' not in produtos)

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)

objeto_celeste = 'galáxia esPiral m31'
print(objeto_celeste.capitalize())
print(objeto_celeste.title())

suplemento = 'cloreto de magnesio'
n_suplemento = suplemento.replace('magnesio', 'zinco')

#antes do replace
print(suplemento)

#depois do replace
print(n_suplemento)

#strip
frase = '      Omega 3 e bom para saude              '
print(frase.strip())

#verifica se a string com um termo em especifico
p = 'Alexandre Berrigue'
print(p.startswith('A'))

#Docstrings
docstring = """
Docstring é uma especie de documentação que podemos
inserir dentro de um módulo, função ou classe em python,
entre outros locais.
    Respeita descolocamento de texto e é    multilinhas
"""

print(docstring)