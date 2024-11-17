#classe modelo apenas para importar
#teste de alteracao ssh

senha = 0
nome = ''
opcao = 0

#identifica nome
def identificaNome():
    nome = input('Digite o seu nome por favor: ')

    if nome == 'Alexandre' or nome == 'alexandre':
        print(f'Nome do lider identificado! {nome}')
        print('Você liberou o acesso VIP!')

        senha = int (input('Agora digite a senha: '))
        if senha == 2030:
            print('Senha correta! Bloco liberado!')
        else:
            print('Opa! Parece que a senha está incorreta!')
            print('Encerrando.')
        
    else:
        print(f'Bem vindo! {nome}')

#Selecionar o opcao
#rodar loop para garantir que o usuario digite o numero valido
while True:
    try:
        opcao = int(input('Digite (1) opcao para iniciar: '))
        if opcao == 1:
            identificaNome()
            break
        else:
            print('FIM')
            break
    except ValueError:
        print('Erro! Por favor, digite um número (1) para iniciar!')
