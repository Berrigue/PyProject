#compreensão de lista

frase = 'A lógica é apenas o principio da sabedoria, e não o seu fim.'
vogais = ['a','e','i','o','u','á','é','í','ó','ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase possui {len(lista_vogais)} vogais:')
print(lista_vogais)


