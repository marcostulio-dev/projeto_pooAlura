from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_pracamineira = Restaurante('Praça Mineira', 'Comida Mineira')
bebida_suco = Bebida('Suco de Melância', 5.0, 'Grande')
prato_entrada = Prato('Entrada de Pães', 2.50, 'Entrada de pães com manteiga')

restaurante_pracamineira.adicionar_no_cardapio(bebida_suco)
restaurante_pracamineira.adicionar_no_cardapio(prato_entrada)

# Parâmetros para avalição:
# restaurante_pracamineira.receber_avaliacao('Marcos', 10)
# restaurante_pracamineira.receber_avaliacao('Lêlê', 8.5)
# restaurante_pracamineira.receber_avaliacao('Dany', 5)


def main():
    
    restaurante_pracamineira.exibir_cardapio

if __name__ == '__main__':
    main()