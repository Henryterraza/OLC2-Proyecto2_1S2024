from interface.instruccion import Instruction
from environment.types import Type,StringType
from environment.symbol import Symbol

class ArrayDeclaration(Instruction):
    def __init__(self, line, col, TipoDec, id, type, exp):
        self.line = line
        self.col = col
        self.TipoDec = TipoDec
        self.id = id
        self.type = type
        self.exp = exp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        # # Obtener simbolo
        # result = self.exp.ejecutar(ast, env)
        # # Validar tipo principal
        # if result.type != Type.ARRAY:
        #     list = ["La expresión no es un arreglo", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return
        # # Validar tipos
        # for res in result.value:
        #     if res.type != self.type and res.type != Type.ARRAY:
        #         list = ["El arreglo contiene tipos incorrectos", env.id, self.line, self.col, "Semantico"]
        #         ast.setErrors(list)
        #         return
            
        # NewSimbol = Symbol(self.line, self.col,  result.value, self.type)

        # result.value = NewSimbol
            
        # contenido = {}

        # contenido[self.TipoDec] = result
        # # Agregar al entorno
        # TipSimb = ""
        # if self.TipoDec == "var":
        #     TipSimb = "variable"
        # else:
        #     TipSimb = "constante"

        # list = [self.id,  TipSimb, StringType.Retorno(result.type.value) , env.id, self.line, self.col]
        # ast.setsimbols(list)

        # env.saveVariable(self.line, self.col, ast, self.id, contenido)
        return None