class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self, largura, profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property
    def profundidade(self):
        return self.__profundidade

    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)
        except Exception:
            print('O valor da largura é invalido!')
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print('O valor da profundidade é invalido!')
            exit()