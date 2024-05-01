from interface.expression import Expression


class OperTern(Expression):
    def __init__(self, line, col, ResLeft, ResRight, condicion):
        self.line = line
        self.col = col
        self.ResLeft = ResLeft
        self.ResRight = ResRight
        self.condicion  = condicion

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):

        #cond = self.condicion.ejecutar(ast, env, gen)






        #     return self.ResLeft.ejecutar(ast, env)
        # else:
        #     return self.ResRight.ejecutar(ast, env)
        return None
