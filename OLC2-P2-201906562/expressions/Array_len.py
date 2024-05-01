from interface.expression import Expression
from environment.types import Type
from environment.symbol import Symbol
from expressions.AccesVarConst import AccessVarConst

class arrayLength(Expression):
    def __init__(self, line, col, Id):
        self.line = line
        self.col = col
        self.Id = Id

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        # # Traer el arreglo
        
        # Id = AccessVarConst(self.line, self.col, self.Id)
        # res = Symbol(self.line, self.col, None, Type.NULL)

        # symArray = Id.ejecutar(ast, env)
        # # Validar tipo principal
        # if symArray.type != Type.ARRAY:
        #     list = ["La variable no es un arreglo", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return res

        # res.value = len(symArray.value.value)
        # res.type = Type.INTEGER 

        # return res
        return None