import os

os.chdir('/home/berrigue/Documentos')
print(f'Diretorio atual: {os.getcwd()}')

padrao_nome = input('Qual o padrão de nomes de arquivos deseja usar (sem extensão)? ')

for contador, arquivo in enumerate(os.listdir()):
    if os.path.isfile(arquivo):
        nome_arquivo, exten_arquivo = os.path.splitext(arquivo)
        nome_arquivo = padrao_nome + ' ' + str(contador)
        
        nome_novo = f'{nome_arquivo}{exten_arquivo}'
        os.rename(arquivo, nome_novo)
        
print(f'\nArquivos renomeados.')