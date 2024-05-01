from interface.expression import Expression
from environment.types import  Type
from environment.symbol import Symbol

class Continue(Expression):
    def __init__(self, line, col):
        self.line = line
        self.col = col

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        
        if env.LoopValidation():
            gen.add_jump(lvlcont)
            return None
        
        list = ["La sentencia de transferencia continue no se encuentra dentro de un ciclo", env.id, self.line, self.col, "Semantico"]
        ast.setErrors(list)
        return None