class Calculadora:
    def __init__(self):
        self.__visor = 0
        self.__anterior = 0
        self.__operador = '+'

    @property
    def visor(self) -> float:
        return self.__visor
    @property
    def anterior(self) -> float:
        return self.__anterior
    @property
    def operador(self) -> float:
        return self.__operador
    
    def somar(self, valor: float) -> float:
        self.__anterior = self.__visor
        self.__visor += valor
        self.__operador = '+'
        return self.__visor, self.__operador
    
    def subtrair(self, valor: float) -> float:
        self.__anterior = self.__visor
        self.__visor -= valor
        self.__operador = '-'
        return self.__visor, self.__operador
    
    def multiplicar(self, valor: float) -> float:
        self.__anterior = self.__visor
        self.__visor *= valor
        self.__operador = '*'
        return self.__visor, self.__operador
    
    def dividir(self, valor: float) -> float:
        self.__anterior = self.__visor
        self.__visor /= valor
        self.__operador = '/'
        return self.__visor, self.__operador

    def resetar(self):
        self.__visor = 0
        return self.__visor 
    
    def voltar(self):
        self.__visor = self.__anterior
        return self.__visor
    
    def exibir(self):
        return self.__visor
