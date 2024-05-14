from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','Gourmet')
restaurante_praca.receber_avaliacao('Chipo',10)
restaurante_praca.receber_avaliacao('Paprio',6)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()