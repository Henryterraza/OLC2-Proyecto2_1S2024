from interface.instruccion import Instruction
from environment.symbol import Symbol
from environment.types import Type, Reser_Words, StringType

class DeclarInterface(Instruction):
    def __init__(self, line,  col, IdVar, IdInter, ListAtrib):
        self.line = line
        self.col = col
        self.IdVar = IdVar
        self.IdInter = IdInter
        self.ListAtrib = ListAtrib

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):

        # if Reser_Words.Verificar(self.IdVar):
        #     list = ["El id ya existe como palabra reservada", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return


        # Interface = env.getInterace(self.line, self.col, ast, self.IdInter)

        # if Interface == None:
        #     list = [f"El interface {self.IdInter} no existe", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return


        # if len(self.ListAtrib) != Interface["size"]:
        #     list = [f"la cantidad de atributos no coinciden con el interface {self.IdInter}", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        # newDicci={}

        # for atributo in self.ListAtrib:
        #     dicInter = Interface["conte"].value
        #     if atributo[0] in dicInter:
        #         respExp = atributo[1].ejecutar(ast, env)

        #         if respExp.type == Type.INTEGER and dicInter[atributo[0]] == Type.FLOAT:
        #             respExp.value = float(respExp.value)
        #             respExp.type = Type.FLOAT
        #             newDicci[atributo[0]] = respExp
        #         elif respExp.type == dicInter[atributo[0]]:
        #             newDicci[atributo[0]] = respExp
        #         else:
        #             list = [f"El atributo {atributo[0]} debe ser de tipo {StringType.Retorno(dicInter[atributo[0]].value)}", env.id, self.line, self.col, "Semantico"]
        #             ast.setErrors(list) 
        #     else:
        #         list = [f"El atributo {atributo[0]} no existe", env.id, self.line, self.col, "Semantico"]
        #         ast.setErrors(list) 


        # contenido = {}

        # contenido["var"] = Symbol(self.line, self.col, newDicci, Interface["conte"].type)

        # list = [self.IdVar,  "var", StringType.Retorno(Interface["conte"].type.value) , env.id, self.line, self.col]
        # ast.setsimbols(list)
        
        # env.saveVariable(self.line, self.col, ast, self.IdVar, contenido)
        return None
