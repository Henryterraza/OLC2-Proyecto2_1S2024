from abc import ABC, abstractmethod

class Instruction(ABC):

    @abstractmethod
    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        pass