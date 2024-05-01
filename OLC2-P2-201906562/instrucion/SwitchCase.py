from interface.instruccion import Instruction
from environment.types import Type


# from expressions.continue_statement import Continue

class SwitchCase(Instruction):
    def __init__(self, line, col, OpExp, InstCase):
        self.line = line
        self.col = col
        self.OpExp = OpExp
        self.InstCase = InstCase
    
    def GetExpresion(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
         rest = self.OpExp.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
         return rest

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno ):

        for case in self.InstCase:
            res = case.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
            
        return None
           
    
  