from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    #Lista onde serão armazenados os restaurantes
    restaurantes = []
    
    #__init__ Define um método contrutor
    def __init__(self, nome, categoria):

        #O self._ é usado para privar os atributos
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        
        return f'{self._nome} | {self._categoria}'
    
    #Este método indica que está função está diretamente ligada a classe
    @classmethod
    #Lista os restaurentes que estão na lista e já os organiza através do .ljus()
    def listar_restaurantes(cls):

        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} | {'Avaliação'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {str(restaurante.media_notas).ljust(25)}')

    #O método @property serve basicamente para definir que a função pode ser acessada com um atributo (getters/setters)
    @property
    def ativo(self):
        
        return '✔️' if self._ativo else '❌'
    
    def alternar_estado(self):
        
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):

        if 0 < nota <= 5:    
            avalicao = Avaliacao(cliente, nota)
            
            self._avaliacao.append(avalicao)

    @property
    def media_notas(self):
        
        if not self._avaliacao:
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantida_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantida_de_notas, 1)

        return media

    def adicionar_no_cardapio(self,item):
        
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        
        print(f'Cardapio Restaurante {self._nome}\n')

        for i, item in enumerate(self._cardapio, start=1):

            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'

                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'

                print(mensagem_bebida)