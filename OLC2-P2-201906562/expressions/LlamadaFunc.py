from interface.expression import Expression
from environment.types import Type,StringType
from environment.symbol import Symbol
from environment.environment import Environment
from instrucion.declaracion import Declaration
from expressions.Return import Return

class LlamaFunc(Expression):
    def __init__(self, line, col, id, ListExp):
        self.line = line
        self.col = col
        self.id = id
        self.ListExp = ListExp

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        # # Realizar busqueda en entorno

        # funcion = env.getFunction(self.line, self.col, ast, self.id)

        # contenido = Symbol(self.line, self.col, None, Type.NULL)
        
        # ListParam = funcion["Param"]

        # envFuncion = Environment(env, "FUNCTION")


        # if len(ListParam) != len((self.ListExp)):
        #     list = [f"Los parametros de la funcion {self.id} no coinciden con los enviados.", envFuncion.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return contenido
        
        # for i in range(len(ListParam)):
        #     exp = self.ListExp[i].ejecutar(ast, envFuncion)
        #     if ListParam[i][1] != exp.type :
        #         list = [f"El parametros {ListParam[i][0]} de la funcion {self.id} solo acepta el tipo {StringType.Retorno(ListParam[i][1].value)}.", envFuncion.id, self.line, self.col, "Semantico"]
        #         ast.setErrors(list)
        #         return contenido
        


        # # se guarda las variables como var  en el etorno de tabla para ser usadas
        # for i in range(len(ListParam)):
        #     contenido = {}

        #     contenido["var"] = self.ListExp[i].ejecutar(ast, env)
        
        #     envFuncion.saveVariable(self.line, self.col, ast, ListParam[i][0], contenido)

        # listInst = funcion["Inst"]
        
        # # if funcion["Return"] != None:
        # #     if not (isinstance(listInst[-1], Return)):
        # #         list = [f"La funcion {self.id} Requiere de un Retorno final.", envFuncion.id, self.line, self.col, "Semantico"]
        # #         ast.setErrors(list)
        # #         return contenido
        

        # for intruc in listInst:
        #     res = intruc.ejecutar(ast, envFuncion)
        #     if res != None:
        #         if res.type == Type.RETURN:
        #             if funcion["Return"] != None :
        #                 ResReturn = res.value.ejecutar(ast, envFuncion)
        #                 if funcion["Return"] == ResReturn.type:
        #                     return ResReturn
        #                 else:
        #                     tipo = funcion["Return"].value
        #                     list = [f"La funcion {self.id} solo retorna tipos {StringType.Retorno(tipo)}.", envFuncion.id, self.line, self.col, "Semantico"]
        #                     ast.setErrors(list)
        #                     return contenido 

        #             else:
        #                list = [f"La funcion {self.id} no permite retornos.", envFuncion.id, self.line, self.col, "Semantico"]
        #                ast.setErrors(list)
        #                return contenido 


        # return contenido
        return None