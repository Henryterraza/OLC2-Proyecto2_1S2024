from interface.instruccion import Instruction
from environment.symbol import Symbol
from environment.types import Type, Reser_Words, StringType, lista

class newtipe():
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __eq__(self, other):
        if isinstance(other, newtipe):
            return self.name == other.name and self.value == other.value
        return False

class Interface(Instruction):
    def __init__(self, line, col, Id, ListAtrib):
        self.line = line
        self.col = col
        self.Id = Id
        self.ListAtrib = ListAtrib

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):


        # if Reser_Words.Verificar(self.Id):
        #     list = ["El id ya existe como palabra reservada", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return


        # new = ""   
        # if self.Id in lista:
        #     new = newtipe(self.Id, lista.index(self.Id))
        # else:
        #     new = newtipe(self.Id, StringType.GetSize())
        #     StringType.Setlist(self.Id)
        

        # DiccInterface = {}

        # for atributo in self.ListAtrib:
        #     if not (atributo[0] in DiccInterface):
        #         DiccInterface[atributo[0]] = atributo[1]
        #     else:
        #         list = [f"El atributo {atributo[0]} del interface {self.Id} se repite", env.id, self.line, self.col, "Semantico"]
        #         ast.setErrors(list)
        #         return
            
        # result = Symbol(self.line, self.col, DiccInterface, new)
        # result = {"size": len(self.ListAtrib), "conte": result}

        # env.saveInterace(self.line, self.col, ast, self.Id, result)
        return None