from interface.expression import Expression
from environment.types import Type, StringType
from environment.symbol import Symbol
from environment.value import Value

from expressions.AccesVarConst import AccessVarConst

class typeof(Expression):
    def __init__(self, line, col, exp):
        self.line = line
        self.col = col
        self.exp = exp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):

        
        # if not isinstance(self.exp, AccessVarConst): 
        #     list = [f"Solo se acepta datos tipo primitivo", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        
        # res = self.exp.ejecutar(ast, env)



        # return Symbol(line=self.line, col=self.col, value= StringType.Retorno(res.type.value), type=Type.STRING)
      
      
      
      
        if not isinstance(self.exp, AccessVarConst): 
            list = [f"Solo se acepta datos tipo primitivo", env.id, self.line, self.col, "Semantico"]
            ast.setErrors(list)
            return Value('msg_null', False, Type.STRING, [],[],[])
        
        res = self.exp.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)


        return Value(str(res.value)+ '.typeof', False, Type.STRING, [], [], [])