from interface.expression import Expression
from environment.types import  Type, StringType
from environment.symbol import Symbol

class ParFloat(Expression):
    def __init__(self, line, col, exp):
        self.line = line
        self.col = col
        self.exp = exp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):

        # res = self.exp.ejecutar(ast, env)
        # Salida = Symbol(line=res.line, col=res.col, value=None, type=Type.NULL)


        # if res.type != Type.INTEGER and res.type != Type.STRING and  res.type != Type.FLOAT:
            
        #     list = [f"El parserfloat no acepta el tipo {StringType.Retorno(res.type.value)}", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)

        # try:
        #     Salida.value = float(res.value)
        # except Exception as e:
        #     list = [f"No se puede parsear la cadena {res.value}", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)

        # Salida.type = Type.FLOAT
    
        # return Salida
        return None