from environment.symbol import Symbol
from environment.types import Type

class Environment():
    def __init__(self, previous, id):
        self.previous = previous
        self.id = id
        self.tabla = {}
        self.interfaces = {}
        self.functions = {}

    def saveInterace(self, lin, col, ast, id, contenido):
        if id in self.interfaces:
            list = [f"La variable {id} ya existe.", self.id, lin, col, "Semantico"]
            ast.setErrors(list)
            return 
        self.interfaces[id] = contenido

    def getInterace(self, lin, col, ast, id):
        tmpEnv = self
        while True:
            if id in tmpEnv.interfaces:
                return tmpEnv.interfaces[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        list = [f"La variable {id} no existe.", self.id, lin, col, "Semantico"]
        ast.setErrors(list)
        return None

    def setInterface(self, lin, col, ast, id, symbol):
        tmpEnv = self
        while True:
            if id in tmpEnv.interfaces:
                tmpEnv.interfaces[id] = symbol
                return
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        list = [f"La variable {id} no existe.", self.id, lin, col, "Semantico"]
        ast.setErrors(list)

    def saveVariable(self, lin, col, ast, id, contenido):
        if id in self.tabla:
            list = [f"La variable {id} ya existe.", self.id, lin, col, "Semantico"]
            ast.setErrors(list)
            return 
        self.tabla[id] = contenido

    def getVariable(self, lin, col, ast, id):
        tmpEnv = self
        while True:
            if id in tmpEnv.tabla:
                return tmpEnv.tabla[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        list = [f"La variable {id} no existe.", self.id, lin, col, "Semantico"]
        ast.setErrors(list)
        return None

    def setVariable(self, lin, col, ast, id, symbol):
        tmpEnv = self
        while True:
            if id in tmpEnv.tabla:
                tmpEnv.tabla[id] = symbol
                return
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        list = [f"La variable {id} no existe.", self.id, lin, col, "Semantico"]
        ast.setErrors(list)
        

    def saveFunction(self, lin, col, ast, id, function):
        if id in self.functions:
            list = [f"Ya existe una función con el nombre {id}", self.id, lin, col, "Semantico"]
            ast.setErrors(list)
            return 
        self.functions[id] = function

    def getFunction(self, lin, col, ast, id):
        tmpEnv = self
        while True:
            if id in tmpEnv.functions:
                return tmpEnv.functions[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        list = [f"La función {id} no existe.", self.id, lin, col, "Semantico"]
        ast.setErrors(list)
        return None

    def LoopValidation(self):
        tmpEnv = self
        while True:
            if tmpEnv.id == 'WHILE' or tmpEnv.id == 'FOR':
                return True
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        return False
    
    def SwitchValidation(self):
        tmpEnv = self
        while True:
            if tmpEnv.id == 'SWITCH':
                return True
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        return False



    def FunctionValidation(self):
        tmpEnv = self
        while True:
            if 'FUNCTION' in tmpEnv.id:
                return True
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        return False
    
    def getGlobalEnvironment(self):
        tmpEnv = self
        while True:
            if tmpEnv.previous == None:
                return tmpEnv
            else:
                tmpEnv = tmpEnv.previous
