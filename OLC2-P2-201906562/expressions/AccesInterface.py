from interface.expression import Expression
from environment.types import Type
from environment.symbol import Symbol
from expressions.AccesVarConst import AccessVarConst
from instrucion.Interface import newtipe

class AccessInterface(Expression):
    def __init__(self, line, col, Exp, IdAtrib):
        self.line = line
        self.col = col
        self.Exp = Exp
        self.IdAtrib = IdAtrib

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        # Realizar busqueda en entorno

        # Id = AccessVarConst(self.line, self.col, self.Exp)
          
        # res = Id.ejecutar(ast, env)

        # if not isinstance(res.type, newtipe):
        #     list = [f"La variables no es de tipo interface", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        

        # if self.IdAtrib in res.value:
        #     return res.value[self.IdAtrib]

        # list = [f"El atributo {self.IdAtrib} no existe", env.id, self.line, self.col, "Semantico"]
        # ast.setErrors(list)
        # return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        return None