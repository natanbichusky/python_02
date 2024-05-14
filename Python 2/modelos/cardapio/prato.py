from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco) #está importando de ItemCardápio
        self.descricao = descricao #essa variável é especifica de prato.py , separado da importacao de ItemCardapio

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco*0.08)