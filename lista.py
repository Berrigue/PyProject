#testando listas em python

n1 = [1,2,3,4,5,6,7,8]
n2 = [10,20,30,40,50,60,70,80]

listaFechada = n1 + n2


#acessar apenas os 4 primeiros numeros da lista
print(listaFechada[:4])

#altera um valor da lista em sua respectiva posicao
listaFechada[-1] = 81

#print(listaFechada)
print(listaFechada[-1])