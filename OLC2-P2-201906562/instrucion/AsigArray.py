from interface.expression import Expression
from environment.types import Type
from environment.symbol import Symbol

class asignArray(Expression):
    def __init__(self, line, col, Id, Index, exp):
        self.line = line
        self.col = col
        self.Id = Id
        self.Index = Index
        self.exp = exp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        # # Traer el arreglo
        # symArray = self.Id.ejecutar(ast, env)
        # # Validar tipo principal
        # if symArray.type != Type.ARRAY:
        #     list = ["La variable no es un arreglo", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        
        # # Validar indice
        # indexVal = self.Index.ejecutar(ast, env)
        # if indexVal.type != Type.INTEGER:
        #     list = ["El indice contiene un valor incorrecto", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return
        # # Retornar valor

       

        # try:
        #     _ = symArray.value.value[indexVal.value]
        # except:
        #     list = ["No existe un vaor en el indice ingresado", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        # ExpVal =  self.exp.ejecutar(ast, env)

        # if symArray.value.type != ExpVal.type:
        #     list = ["El valor a asignar no son des mismo tipo", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return


        # symArray.value.value[indexVal.value] = ExpVal
        return None
