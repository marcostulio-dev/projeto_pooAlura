from modelos.cardapio.item_cardapio import ItemCardapio

#Classe filha (herdando atributos da classe mãe)
class Prato(ItemCardapio):

    def __init__(self, nome, preco, descricao):
        
        #Função necessária para aplicar a herança
        super().__init__(nome, preco) #Atributos que serão herdados
        #Atributo original da classe filha
        self.descricao = descricao

    def __str__(self):

        return self._nome
    
    #Criação da função que gerará o polimorfismo
    def aplicar_desconto(self):
        
        self._preco -= (self._preco * 0.08)