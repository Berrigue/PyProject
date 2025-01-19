#Trocar valores entre duas variaveis

var1 = 12
var2 = 31

menor = var1 if var1 < var2 else var2
print(f'Menor valor:{menor}')
print(f'Menor valor: {(var2, var1)[var1 < var2]}')

# Função enumerate ()

bebidas = ['Café','Chá','Água', 'Suco', 'Refrigerante']
for i, item in enumerate(bebidas):
    print(f'Indice: {i}, Item: {item}')