from interface.instruccion import Instruction
from environment.types import Type, TypeAritmetica
from expressions.primitive import Primitive
from expressions.aritmetica import Aritmetica
from instrucion.Interface import newtipe

class AsigInterface(Instruction):
    def __init__(self, line, col, Id, IdAtrib, ExpAsig, operacion):
        self.line = line
        self.col = col
        self.Id = Id
        self.IdAtrib = IdAtrib
        self.ExpAsig = ExpAsig
        self.operacion = operacion

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        # # Realizar busqueda en entorno

        
        # Existid = env.getVariable(self.line, self.col, ast, self.Id)

        # if Existid == None:
        #     return
        
        # res = Existid["var"]
    

        # if not isinstance(res.type, newtipe):
        #     list = [f"La variables no es de tipo interface", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return 

        # if not (self.IdAtrib in res.value):
        #     list = [f"El atributo {self.IdAtrib} no existe", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return 
        
        # respAtribAsig = self.ExpAsig.ejecutar(ast, env)

        # if res.value[self.IdAtrib].type == Type.FLOAT and respAtribAsig.type == Type.INTEGER:
        #     res.value[self.IdAtrib].value = float(res.value[self.IdAtrib].value)
        #     res.value[self.IdAtrib].type = Type.FLOAT
        # elif res.value[self.IdAtrib].type != respAtribAsig.type: 
        #     list = [f"El valor a asignar al atributo {self.IdAtrib} no son iguales", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        # symL = Primitive(self.line, self.col, res.value[self.IdAtrib].value, res.value[self.IdAtrib].type)
        # symR = Primitive(self.line, self.col, respAtribAsig.value, respAtribAsig.type)
                    
        

        # if self.operacion == TypeAritmetica.SUMA:
        #         res.value[self.IdAtrib] = Aritmetica(self.line, self.col, symL, symR, TypeAritmetica.SUMA).ejecutar(ast, env)
        # elif self.operacion == TypeAritmetica.RESTA:
        #         res.value[self.IdAtrib] = Aritmetica(self.line, self.col, symL, symR, TypeAritmetica.RESTA).ejecutar(ast, env)
        # else:
        #     res.value[self.IdAtrib] = respAtribAsig


        # Existid["var"] = res

        # env.setVariable(self.line, self.col, ast, self.Id, Existid)

        # return 
        return None

       