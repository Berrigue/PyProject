# Orientação a objetos: Paradigma de programação
# Classes e Objetos    

class Veiculo:
            
    def movimentar(self):
        print(f'Sou um veículo é me desloco!')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None
        
    # Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro
    
    # Getter    
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')        
    
    # Getter
    def get_num_registro(self):
        return self.__num_registro
    
class Carro(Veiculo):
    # o Método __init__ será herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas')
        
class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Sou uma moto é Corro muito!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__categoria = categoria
        super().__init__(fabricante, modelo)
        
    # Getter
    def get_categoria(self):
        return self.__categoria
    
    # Getter
    def movimentar(self):
        print('Eu voo alto!')
    
if __name__=='__main__':
    # meu_veiculo = Veiculo('GM', 'cadillac Escalade')
    # meu_veiculo.movimentar()  
    # meu_veiculo.get_fabr_modelo()
    # meu_veiculo.set_num_registro('49557-1')
    # print(f'Esse é o número do meu registro {meu_veiculo.get_num_registro()}')
    
    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()
    
    seu_carro = Carro('Audi', 'A5 Sportback')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()
    
    moto = Motocicleta('BMW', 'Bis')
    moto.movimentar()
    moto.get_fabr_modelo()
    
    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')