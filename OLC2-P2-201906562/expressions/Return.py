from interface.expression import Expression
from environment.types import  Type
from environment.symbol import Symbol

class Return(Expression):
    def __init__(self, line, col, exp):
        self.line = line
        self.col = col
        self.exp = exp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        if env.FunctionValidation():
            if self.exp == None:
                gen.add_jump(lvlreturno)
                return None
            #Falta colocar en a0 el resultado del retorno siendo un entero o flotante dependiendo de la funcion que valor a devolver
            gen.add_jump(lvlreturno)
            return None
        
        list = ["La sentencia de transferencia return no se encuentra dentro de una funcion", env.id, self.line, self.col, "Semantico"]
        ast.setErrors(list)
 
        return None
  