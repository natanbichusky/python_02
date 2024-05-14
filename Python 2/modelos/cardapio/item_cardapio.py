from abc import ABC, abstractmethod #para criar um método abstrato - no caso seria aplicar desconto, ela poderá ser aplicada em qualquer classe quando quiser usá-la
#não significa necessariamente que será usada

class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def aplicar_desconto(self):
        pass