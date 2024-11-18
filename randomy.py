import random as ran

# print('Gerar cinco números aleatorios entre 1 e 50: \n')
# for i in range(5):
#     n = ran.randint(1,50)
#     print(f'Número gerado: {n}')

# valor = ran.random()
# print(f'Número gerado: {round(valor *10,2)}')

# valor = ran.uniform(1,100)
# print(f'Número: {round(valor, 4)}')

L = [2,4,6,7,8,9,10,11,15,47,44,66,88,100,105,500,600,800]
# n = ran.choice(L)

# print(f'Número escolhido: {n}')

# n = ran.sample(L,3)
# print(f'Números escolhidos: {n}')

#embaralhar lista
print(f'Exibir lista original: {L}')
print('Embaralhar a lista e exibi-la:')

n = ran.shuffle(L)
print(L)