from modelos.cardapio.item_cardapio import ItemCardapio

#Classe filha (herdando atributos da classe mãe)
class Bebida(ItemCardapio):

    def __init__(self, nome, preco, tamanho):
        
        #Função necessária para aplicar a herança
        super().__init__(nome, preco) #Atributos que serão herdados
        #Atributo original da classe filha
        self.tamanho = tamanho 

    def __str__(self):

        return self._nome
    
    #Aplicação do polimorfismo
    def aplicar_desconto(self):
        
        self._preco -= (self._preco * 0.05)