from decimal import Decimal

# Programa que simula uma catraca bem FULERA! 
# Configurações iniciais
Catraca = True
CatracaCount = 0
tarifa = Decimal('7.90')
carteira = Decimal('10.00')

if __name__ == "__main__":
    print('Iniciando o programa...')
    
    while Catraca:
        print('\n--- Nova interação ---')
        print(f'Saldo atual da carteira: R$ {carteira:.2f}')
        
        # Verifica se a catraca está liberada
        if Catraca:
            print('OK! Catraca está liberada. Pode passar!')
            name = input('Qual o seu nome? ')
            print(f'Muito bem-vindo(a), {name}!')
            print(f'A passagem custa R$ {tarifa:.2f}. Posso cobrar?')
            
            resposta = input('Digite SIM ou NÃO: ').upper()
            
            if resposta == 'SIM':
                if carteira >= tarifa:
                    carteira -= tarifa
                    CatracaCount += 1
                    print(f'Muito bem! Cobramos R$ {tarifa:.2f} da sua carteira.')
                    print(f'Saldo atual da carteira: R$ {carteira:.2f}')
                    print('Você passou pela catraca!')
                else:
                    print('Saldo insuficiente. Você não pode passar.')
            elif resposta == 'NÃO' or resposta == 'NAO':
                print(f'OK, você escolheu não pagar. Saldo atual da carteira: R$ {carteira:.2f}')
            else:
                print('Resposta inválida. Digite "SIM" ou "NÃO".')
        
        # Pergunta se deseja continuar
        continuar = input('Deseja continuar? (SIM/NÃO): ').upper()
        if continuar != 'SIM':
            Catraca = False
    
    # Resultado final
    print('\n--- Fim do programa ---')
    print(f'Total de pessoas que passaram pela catraca: {CatracaCount}')