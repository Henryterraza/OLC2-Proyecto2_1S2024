from interface.expression import Expression
from environment.types import Type
from environment.symbol import Symbol
from environment.environment import Environment
from environment.generator import Generator
from environment.value import Value

class AccessVarConst(Expression):
    def __init__(self, line, col, id):
        self.line = line
        self.col = col
        self.id = id

    def ejecutar(self, ast, env: Environment, gen:Generator, lvlbreak, lvlcont, lvlreturno ):
        # Realizar busqueda en entorno
        Existid = env.getVariable(self.line, self.col, ast, self.id)

        # contenido = Symbol(self.line, self.col, None, Type.NULL)
        contenido = Value('msg_null', False, Type.NULL, [], [], [])

        if Existid == None:
            return contenido

        if "var" in Existid:
            contenido = Existid["var"]
        else:
            contenido = Existid["const"]

            
        return contenido

