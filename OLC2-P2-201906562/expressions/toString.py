from interface.expression import Expression
from environment.types import  Type
from environment.symbol import Symbol
from expressions.primitive import Primitive
from expressions.AccesVarConst import AccessVarConst

class toString(Expression):
    def __init__(self, line, col, exp):
        self.line = line
        self.col = col
        self.exp = exp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):

    
        # res = None

        # if isinstance(self.exp, Primitive):
        #     res = self.exp.ejecutar(ast, env)
        #     if res.type != Type.BOOLEAN:
        #         list = [f"No se puede parsear {res.value} a cadena", env.id, self.line, self.col, "Semantico"]
        #         ast.setErrors(list)
        #         return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        # else:
        #     Id = AccessVarConst(self.line, self.col, self.exp)
        #     res = Id.ejecutar(ast, env)
        
        # Salida = Symbol(line=res.line, col=res.col, value=None, type=Type.NULL)

        # try:
        #     Salida.value = str(res.value)
        # except Exception as e:
        #     list = [f"No se puede parsear {res.value} a cadena", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)

        # Salida.type = Type.STRING
    
        # return Salida
        return None