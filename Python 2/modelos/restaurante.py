from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):  #self é a mesma coisa que usar "this"
        self._nome = nome.title()  #upper para deixar a  primeira letra maiuscula 
        self._categoria = categoria.upper()  #upper para deixar a letra maiuscula 
        self._ativo = False   #O _ serve para deixar o atributro protegido
        self._avaliacao = []    #gera lista para armazenar as avaliações
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__ (self):
        return f'{self.nome} | {self.categoria}' #pra transformar em string a informação ao invés de dados

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante: '.ljust(25)} | {'Categoria: '.ljust(25)} | {'Avaliação: '.ljust(25)} | {'Status: '.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self): #método para os objetos
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #sum soma das notas na lista
        quantidade_de_notas = len(self._avaliacao) #len conta quantidade de notas para calcular a média
        media = round(soma_das_notas/quantidade_de_notas, 1) #round arredonda o resultado para ter apenas uma cada decimal (o 1 referencia 1 casa decimal)
        return media

#   def adicionar_bebida_cardapio(self, bebida):
#      self._cardapio.append(bebida)

#   def adicionar_prato_cardapio(self, prato):
#       self._cardapio.append(prato)
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio): #verifica se é instancia, se bate com as exigências de ItemCardapio
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio Restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio,start = 1): #para cada item que possa ser numerado em cardapio , começar do 1
            if hasattr(item, 'descricao'): #se o item possui o atributo descrição (acrescentar as outas variaveis descr e tamanho)
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)