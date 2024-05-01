from interface.expression import Expression
from environment.types import Type

class tipo(Expression):
    def __init__(self, line, col, value, type):
        self.line = line
        self.col = col
        self.value = value
        self.type = type

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        return 