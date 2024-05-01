from interface.instruccion import Instruction
from environment.types import Type
from expressions.AccesVarConst import AccessVarConst

class arraypush(Instruction):
    def __init__(self, line, col, Id, exp):
        self.line = line
        self.col = col
        self.Id = Id
        self.exp = exp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        # Traer el arreglo
        
        # Id = AccessVarConst(self.line, self.col, self.Id)

        # symArray = Id.ejecutar(ast, env)
        # # Validar tipo principal
        # if symArray.type != Type.ARRAY:
        #     list = ["La variable no es un arreglo", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        

        # ExpVal =  self.exp.ejecutar(ast, env)

        # if symArray.value.type != ExpVal.type:
        #     list = ["El tipo del valor a asignar no es del tipo del array", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        # symArray.value.value.append(ExpVal)
        return None

        
        

        
