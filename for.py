#brincando com for
alfabeto = []

print('Iniciando o sistema...')

for i in range(3):
    print('Digite suas letras preferidas do alfabeto:')
    letras = input()
    alfabeto.append(letras)

print('\nLetras escolhidas')
for letras in alfabeto:
    print(letras)