from interface.expression import Expression
from environment.types import Type
from environment.symbol import Symbol

class ArrayAccess(Expression):
    def __init__(self, line, col, array, index):
        self.line = line
        self.col = col
        self.array = array
        self.index = index

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        # # Traer el arreglo
        # res = Symbol(self.line, self.col, None, Type.NULL)
        # sym = self.array.ejecutar(ast, env)
        # # Validar tipo principal
        # if sym.type != Type.ARRAY:
        #     list = ["La variable no es un arreglo", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return res
        # # Validar indice
        # indexVal = self.index.ejecutar(ast, env)
        # if indexVal.type != Type.INTEGER:
        #     list = ["El indice contiene un valor incorrecto", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return res
        # # Retornar valor

       

        # try:
        #     res = sym.value.value[indexVal.value]
        # except:
        #     list = ["No existe un vaor en el indice ingresado", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return res

        # return res

        return None


