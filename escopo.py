# Escopo Global e Local

var_global = "Curso completo de Python"

def escrever_texto():
    global var_global
    var_global = "Banco de dados com SQL"
    print(f'Variavel Global: {var_global}')
    #print(f'Variavel Local: {var_local}')


if __name__ == '__main__':
    print(f'Executar a funcção esreve_texto()')
    escrever_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variavel Global: {var_global}')