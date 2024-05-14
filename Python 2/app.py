from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio import item_cardapio

restaurante_praca = Restaurante('praça','Gourmet')
bebida_suco = Bebida('Suco de Laranja',5.0,'Grande')
bebida_suco.aplicar_desconto()
prato_bife = Prato('Bife a parmeggiana',50.0,'Bifao dahora com molho')
prato_bife.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_bife)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()