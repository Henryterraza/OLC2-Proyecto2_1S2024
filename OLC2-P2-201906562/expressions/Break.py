from interface.expression import Expression
from environment.types import Type
from environment.value import Value
from environment.generator import Generator

class Break(Expression):
    def __init__(self, line, col):
        self.line = line
        self.col = col

    def ejecutar(self, ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):

        if env.SwitchValidation():
            gen.add_jump(lvlbreak)
            return None
        
        if env.LoopValidation():
            gen.add_jump(lvlbreak)
            return None
            
        list = ["La sentencia de transferencia break no se encuentra dentro de un switch o ciclo", env.id, self.line, self.col, "Semantico"]
        ast.setErrors(list)

        return None