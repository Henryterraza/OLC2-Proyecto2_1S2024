from interface.instruccion import Instruction
from environment.types import Type
from environment.symbol import Symbol

class Array(Instruction):
    def __init__(self, line, col, list_exp):
        self.line = line
        self.col = col
        self.list_exp = list_exp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        # # Array valor
        # arrVal = []
        # # Recorrer el arreglo
        # for exp in self.list_exp:
        #     indexExp = exp.ejecutar(ast, env)
        #     arrVal.append(indexExp)
            
        # return Symbol(line=self.line, col=self.col, value=arrVal, type=Type.ARRAY)
        return None
        