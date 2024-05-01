from abc import ABC, abstractmethod

class Expression(ABC):

    @abstractmethod
    def ejecutar(self, ast, context, gen, lvlbreak, lvlcont, lvlreturno):
        pass