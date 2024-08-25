from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_pracamineira = Restaurante('Praça Mineira', 'Comida Mineira')
bebida_suco = Bebida('Suco de Melância', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_entrada = Prato('Entrada de Pães', 2.50, 'Entrada de pães com manteiga')
prato_entrada.aplicar_desconto()

restaurante_pracamineira.adicionar_no_cardapio(bebida_suco)
restaurante_pracamineira.adicionar_no_cardapio(prato_entrada)

def main():
    
    restaurante_pracamineira.exibir_cardapio

if __name__ == '__main__':
    main()