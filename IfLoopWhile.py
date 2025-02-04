#ifLoopWhile

#funcão que adiciona um contador de erros nas tryes
def trys():
    
    tryes = 0 # Adiciona um contador de tentativas
    
    while True:
        try1 = str(input('Digite a letra mais bonita do alfabeto: '))
        if try1.upper() == 'A':  # Converte a entrada para maiúscula para evitar erros de case sensitivity
            print('Parabéns! Resposta correta!')
            break  # Sai do loop se a resposta estiver correta
        else:
            tryes += 1 #Incrementando contador de tentativas
            print(f'Resposta incorreta! Tentativas restantes {3 - tryes}')
            if(tryes == 3):
            
                print(f'Parece que você errou todas as tentativas! Bye Bye!')
                exit() 
        
# inicio do programa #main

if __name__ == "__main__":
    print(f'-Informe os seus dados-')

    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))

    if idade >= 18:
        print(f'Sua idade é {idade}. Você pode passar!')
    elif nome == 'Alexandre':
        print(f'Olá, Senhor Alexandre! Parece que é você!')
        print(f'Antes vamos fazer alguns testes...')
        trys()
    else:
        print(f'Sua idade é {idade}. Você é menor de idade.')