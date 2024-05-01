from interface.instruccion import Instruction
from environment.types import Type


# from expressions.continue_statement import Continue

class SwitchDef(Instruction):
    def __init__(self, line, col, InstDef):
        self.line = line
        self.col = col
        self.InstDef = InstDef
    

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        for case in self.InstDef:
            res = case.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)

        
        return None
           
    
  