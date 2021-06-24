from random import randint

class Calcular:

    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3) #1 - Somar, 2 - Diminuir, 3 - Multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    @property
    def _gerar_valor(self: object) -> int:
        pass

    @property
    def _gerar_resultado(self: object) -> int:
        pass

    def checar_resultado(self: object, resposta: int) -> bool:
        pass

    def mostrar_operacao(self: object) -> None:
        pass

    def __str__(self: object) -> str:
        op: str = ''
        operacoes: list = ["Somar", "Diminuir", "Multiplicar"]
        op = str(operacoes[self.operacao - 1])
        return f'Valor 1: {self.valor1}\n' \
               f'Valor 2: {self.valor2}\n' \
               f'Dificuldade: {self.dificuldade}\n' \
               f'Operação: {op}'

