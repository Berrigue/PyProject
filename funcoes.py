# Funcões
# São importantes pela modularização, Reúso de Código, Legibilidade de seu programa.

# def mult(a, b):
#     return a * b

# a = 10
# b = 11

# c = mult (a, b)

#print(f'O produto de  {a} e {b} é {c}')

# def div(k, j):
#     if j!=0:
#      return k / j
#     else:
#        return 'Impossivel dividir por ZERO!'


# #define o ponto inicial de um programa
# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite outro número: '))

#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}')

# def quadrado(val):
#    quadrados = []
#    for x in val:
#       quadrados.append(x ** 2)
#    return quadrados

# if __name__ == '__main__':
   
#    valores = [2,5,7,9,12]
#    resultados = quadrado(valores)
#    for g in resultados:
#       print(g)

#funcao com resultado variavel de acordo com o argumento passado

x = 5
y = 6
z = 3

def soma_mult(a, b, c = 0):
   if c == 0:
      return a * b
   else:
      return a + b + c
   
if __name__ == '__main__':
   res = soma_mult(x,y,z)
   print(res)