#testando listas em python

n1 = [1,2,3,4,5,6,7,8]
n2 = [10,20,30,40,50,60,70,80]

listaFechada = n1 + n2

#inserir um novo elemento a lista na posicao especifica
listaFechada.insert(10, 100)

#inserir um novo elemento a lista
listaFechada.append(400)

#remover um elemento da lista sendo o ultimo da lista
listaFechada.pop()

#remove um elemento da lista na posicao definida
listaFechada.pop(5)

#acessar apenas os 4 primeiros numeros da lista
#print(listaFechada[:4])

#altera um valor da lista em sua respectiva posicao
#listaFechada[-1] = 81

#print(listaFechada)
#print(listaFechada[-1])

#slicing
#print(listaFechada[3:10])

#exibe lista com valores reversos
#print(sorted(listaFechada, reverse = True))

# #mostra quantos numeros tem na lista
# print(len(listaFechada))
# #mostra o menor valor da lista
# print(min(listaFechada))
# #mostrar o maior valor da lista
# print(max(listaFechada))
# #somar valores de uma lista
# print(sum(listaFechada))
# print(listaFechada)

# #verifica se um elemento especifico está dentro da lista
# print(12 in listaFechada)

# planetas = ['terra','marte','plutao','venus','mercurio','uranu',]
# for planeta in planetas:
#     print(planeta)

bebidas = []

for i in range(5):
    print('Digite o nome de 5 bebidas!: ')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)

print('Saude!')


