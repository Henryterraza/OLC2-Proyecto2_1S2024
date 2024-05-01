from interface.instruccion import Instruction
from environment.types import StringType
from environment.generator import Generator
from expressions.aritmetica import Aritmetica
from expressions.primitive import Primitive
from environment.environment import Environment


class Funciones(Instruction):
    def __init__(self, line, col, id, ListPar, TypeReturn, ListIntrucc):
        self.line = line
        self.col = col
        self.id = id
        self.ListPar = ListPar
        self.TypeReturn = TypeReturn
        self.ListIntrucc = ListIntrucc

    def ejecutar(self, ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):
        

        # if env.id != "GLOBAL":
        #     list = [f"Las funciones solo pueden definirse en el ambito global.", self.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        # diccFunc = {}
        # diccFunc["Param"] = self.ListPar
        # diccFunc["Return"] = self.TypeReturn
        # diccFunc["Inst"] = self.ListIntrucc

        # if self.TypeReturn != None:
        #     list = [self.id,  "funcion", StringType.Retorno(self.TypeReturn.value) , env.id, self.line, self.col]
        #     ast.setsimbols(list)
        # else:
        #     list = [self.id,  "funcion", "" , env.id, self.line, self.col]
        #     ast.setsimbols(list)


        # env.saveFunction(self.line, self.col, ast, self.id, diccFunc)
       
       
       
       
       
       
        if env.id != "GLOBAL":
            list = [f"Las funciones solo pueden definirse en el ambito global.", self.id, self.line, self.col, "Semantico"]
            ast.setErrors(list)
            return

        diccFunc = {}
        diccFunc["Param"] = self.ListPar
        diccFunc["Return"] = self.TypeReturn
        diccFunc["value"] = self.id

        if self.TypeReturn != None:
            list = [self.id,  "funcion", StringType.Retorno(self.TypeReturn.value) , env.id, self.line, self.col]
            ast.setsimbols(list)
        else:
            list = [self.id,  "funcion", "" , env.id, self.line, self.col]
            ast.setsimbols(list)


        newgen = Generator(gen.get_contemp, gen.get_contlvl, gen.get_conflo, gen.get_constr )
        

        newgen.new_body_label(self.id)

        envFuncion = Environment(env, "FUNCTION")

        # se guarda las variables como var  en el etorno de tabla para ser usadas
        for i in range(len(self.ListPar)):
            contenido = {}

            contenido["var"] = self.ListExp[i].ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
        
            envFuncion.saveVariable(self.line, self.col, ast, ListParam[i][0], contenido)


        

        







        env.saveFunction(self.line, self.col, ast, self.id, diccFunc)
        
        
        
        return None

