from interface.expression import Expression
from environment.types import Type
from environment.symbol import Symbol
from expressions.AccesVarConst import AccessVarConst


class Indexof(Expression):
    def __init__(self, line, col, Id, exp):
        self.line = line
        self.col = col
        self.Id = Id
        self.exp = exp

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

        # valExp = self.exp.ejecutar(ast, env)
        # for i, valor in enumerate(symArray.value.value):
        #     if valor.value ==  valExp.value:
        #         res.value = i
        #         res.type = Type.INTEGER
        #         return res

        # res.value = -1
        # res.type = Type.INTEGER

        # return res
        return None
