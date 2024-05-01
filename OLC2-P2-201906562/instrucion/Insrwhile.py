from interface.instruccion import Instruction
from environment.environment import Environment
from environment.types import Type
from environment.generator import Generator


class While(Instruction):
    def __init__(self, line, col, exp, InstWhile):
        self.line = line
        self.col = col
        self.exp = exp
        self.InstWhile = InstWhile

    def ejecutar(self, ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):
 
        # while_env = Environment(env, "WHILE")

        # while (True):
        #     devuelto = self.exp.ejecutar(ast, while_env)
            
        #     if not devuelto.value:
        #         break

        #     for inst in self.InstWhile:
        #         res = inst.ejecutar(ast, while_env)
        #         if res != None:
        #             if  res.type == Type.BREAK :
        #                 return None
        #             elif res.type == Type.CONTINUE:
        #                 break
        #             elif res.type == Type.RETURN:
        #                 return res


        while_env = Environment(env, "WHILE")



        lvlInitBucle = gen.new_label()
        lvlExitBucle = gen.new_label()

        gen.comment('instruccion while')

        gen.new_body_label(lvlInitBucle)
        
        devuelto = self.exp.ejecutar(ast, while_env, gen, lvlbreak, lvlcont, lvlreturno)
        
        if devuelto.isTemp:
            if 't' in str(devuelto.value):
                gen.add_move('t3', str(devuelto.value))
            else:
                gen.add_li('t3', str(devuelto.value))
            #gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
        else:
            gen.add_lw('t1', str(devuelto.value))

        gen.add_beqz('t1', lvlExitBucle)

        for inst in self.InstWhile:
            res = inst.ejecutar(ast, while_env, gen, lvlExitBucle, lvlInitBucle, lvlreturno)

        gen.add_jump(lvlInitBucle)
                    
        gen.new_body_label(lvlExitBucle)


        return None 


            

