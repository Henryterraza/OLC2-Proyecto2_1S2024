from interface.instruccion import Instruction
from environment.execute import StatementExecuter
from environment.environment import Environment
from environment.types import Type
from environment.generator import Generator
from environment.value import Value

# from expressions.continue_statement import Continue

class If(Instruction):
    def __init__(self, line, col, exp, InstIf, InstElse, InstEl_If):
        self.line = line
        self.col = col
        self.exp = exp
        self.InstIf = InstIf
        self.InstElse = InstElse
        self.InstEl_If = InstEl_If

    def ejecutar(self, ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):
        # # Obtener simbolo
        

        # if validate.value:
        #     # Crear entorno del If
        #     if_env = Environment(env, "IF")
            
        #     for inst in self.InstIf:
        #         res = inst.ejecutar(ast, if_env)
        #         if res != None:
        #             if res.type == Type.CONTINUE or res.type == Type.BREAK or res.type == Type.RETURN :
        #                 return res
        #     return None
        
        # if self.InstElse != None:
        #     else_env = Environment(env, "ELSE")
            
        #     for inst in self.InstElse:
        #         res = inst.ejecutar(ast, else_env)
        #         if res != None:
        #             if res.type == Type.CONTINUE or res.type == Type.BREAK or res.type == Type.RETURN :
        #                 return res

        # if self.InstEl_If != None:
        #     res = self.InstEl_If.ejecutar(ast, env)
        #     if res != None:
        #             if res.type == Type.CONTINUE or res.type == Type.BREAK or res.type == Type.RETURN :
        #                 return res

        # return None

        GetCond = self.exp.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)


        label1 = gen.new_label()
        label2 = gen.new_label()



        gen.add_li('t3', str(GetCond.value))
        gen.add_lw('t0', '0(t3)')
        gen.comment('Se verifica si cumple la condicion')
        gen.add_beqz('t0', label1)

        if_env = Environment(env, "IF")

        for inst in self.InstIf:
            res = inst.ejecutar(ast, if_env, gen, lvlbreak, lvlcont, lvlreturno)
            if res != None:
                if res.type == Type.CONTINUE or res.type == Type.BREAK or res.type == Type.RETURN :
                    return res
                
        gen.add_jump(label2)

        gen.new_body_label(label1)

        if self.InstElse != None:
            else_env = Environment(env, "ELSE")
            
            
            for inst in self.InstElse:
                res = inst.ejecutar(ast, else_env, gen, lvlbreak, lvlcont, lvlreturno)
                if res != None:
                    if res.type == Type.CONTINUE or res.type == Type.BREAK or res.type == Type.RETURN :
                        return res
                    
            

        if self.InstEl_If != None:
            res = self.InstEl_If.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
            if res != None:
                    if res.type == Type.CONTINUE or res.type == Type.BREAK or res.type == Type.RETURN :
                        return res

        gen.new_body_label(label2)
        
        return None
