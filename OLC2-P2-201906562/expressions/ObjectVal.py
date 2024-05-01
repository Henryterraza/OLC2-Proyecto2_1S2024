from interface.expression import Expression
from environment.types import Type
from environment.symbol import Symbol

from expressions.AccesVarConst import AccessVarConst

class ObjectVal(Expression):
    def __init__(self, line, col, exp):
        self.line = line
        self.col = col
        self.exp = exp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):

        # res = self.exp.ejecutar(ast, env)
        # Salida = Symbol(line=res.line, col=res.col, value=None, type=Type.NULL)

        # if not isinstance(self.exp, AccessVarConst): 
        #     list = [f"Solo se acepta variables ", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        

        # if res.type == Type.STRING or res.type == Type.INTEGER or res.type == Type.FLOAT or res.type == Type.ARRAY or res.type == Type.BOOLEAN or res.type == Type.CHAR: 
        #     list = [f"Solo se acepta tipos interface", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)


        
        # array = []
        # for attri in res.value:
        #     temp = res.value[attri]
        #     array.append(temp)

        # Salida = Symbol(self.line, self.col, array, Type.ARRAY)
        
    
        # return Salida
        return None