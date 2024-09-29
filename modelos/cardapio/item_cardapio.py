#Biblioteca necessária para utilizar o método de polimorfismo
from abc import ABC, abstractmethod

#Classe mãe
class ItemCardapio(ABC):
    
    def __init__(self, nome, preco):
        
        self._nome = nome
        self._preco = preco

    #Criação da função que gerará o polimorfismo
    @abstractmethod
    def aplicar_desconto(self):
        pass      