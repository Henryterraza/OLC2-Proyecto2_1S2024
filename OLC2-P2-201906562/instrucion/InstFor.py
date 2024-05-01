from interface.instruccion import Instruction
from environment.environment import Environment
from environment.types import Type
from environment.generator import Generator
from expressions.AccesVarConst import AccessVarConst


class For(Instruction):
    def __init__(self, line, col, decla, TipoVAR, IDFirst, IDSecond, IDThrird, StartCiclo, EndCiclo, InstFor):
        self.line = line
        self.col = col
        self.decla = decla
        self.TipoVAR = TipoVAR
        self.IDFirst = IDFirst
        self.IDSecond = IDSecond
        self.IDThrird = IDThrird
        self.StartCiclo = StartCiclo
        self.EndCiclo = EndCiclo
        self.InstFor = InstFor


    def ejecutar(self, ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):

        # for_env = Environment(env, "FOR")

        # endFor = self.EndCiclo.ejecutar(ast, for_env)
        # StartFor = self.StartCiclo.ejecutar(ast, for_env)

        # if self.TipoVAR != Type.INTEGER:
        #     list = ["La variable del for solo puede ser de tipo number", for_env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        # if endFor.type != Type.INTEGER and StartFor.type != Type.INTEGER:
        #     list = ["El rango del for solo acepta tipo number", for_env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return
 
        # if self.IDFirst != self.IDSecond and self.IDFirst != self.IDThrird:
        #     list = ["Los id deben ser iguales", for_env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return
        
        # #Se crea la variable en su entorno
        # self.decla.ejecutar(ast, for_env)

        # while (True):
            
            
        #     devuelto = AccessVarConst(self.line, self.col, self.IDFirst).ejecutar(ast, for_env)

        #     if devuelto.value > endFor.value:
        #         break

        #     for inst in self.InstFor:
        #         res = inst.ejecutar(ast, for_env)
        #         if res != None:
        #             if  res.type == Type.BREAK :
        #                 return None
        #             elif res.type == Type.CONTINUE:
        #                 break
        #             elif res.type == Type.RETURN:
        #                 return res 
            
        #     devuelto.value = devuelto.value + 1
        #     dicciSym = {}
        #     dicciSym["const"] = devuelto
        #     for_env.setVariable(devuelto.line, devuelto.col, ast, self.IDFirst, dicciSym)
        





        for_env = Environment(env, "FOR")


        if self.TipoVAR != Type.INTEGER:
            list = ["La variable del for solo puede ser de tipo number", for_env.id, self.line, self.col, "Semantico"]
            ast.setErrors(list)
            return
 
        if self.IDFirst != self.IDSecond and self.IDFirst != self.IDThrird:
            list = ["Los id deben ser iguales", for_env.id, self.line, self.col, "Semantico"]
            ast.setErrors(list)
            return
        
        endFor = self.EndCiclo.ejecutar(ast, for_env, gen, lvlbreak, lvlcont, lvlreturno)
        StartFor = self.StartCiclo.ejecutar(ast, for_env, gen, lvlbreak, lvlcont, lvlreturno)

        if endFor.type != Type.INTEGER and StartFor.type != Type.INTEGER:
            list = ["El rango del for solo acepta tipo number", for_env.id, self.line, self.col, "Semantico"]
            ast.setErrors(list)
            return
        #Se crea la variable en su entorno
        self.decla.ejecutar(ast, for_env, gen, lvlbreak, lvlcont, lvlreturno)

        lvlInitBucle = gen.new_label()
        lvlcontinue = gen.new_label()
        lvlExitBucle = gen.new_label()

        temp = gen.new_temp()
        gen.add_br()
        gen.comment('Agregando un primitivo numerico')
        gen.add_li('t0', '1')
        gen.add_li('t3', str(temp))
        gen.add_sw('t0', '0(t3)')


        gen.comment('instruccion for')

        gen.new_body_label(lvlInitBucle)
            
        devuelto = AccessVarConst(self.line, self.col, self.IDFirst).ejecutar(ast, for_env, gen, lvlbreak, lvlcont, lvlreturno)

        if devuelto.isTemp:
            if 't' in str(devuelto.value):
                gen.add_move('t3', str(devuelto.value))
            else:
                gen.add_li('t3', str(devuelto.value))
            #gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
        else:
            gen.add_lw('t1', str(devuelto.value))

        if endFor.isTemp:
            if 't' in str(endFor.value):
                gen.add_move('t3', str(endFor.value))
            else:
                gen.add_li('t3', str(endFor.value))
            #gen.add_li('t3', str(op1.value))
            gen.add_lw('t2', '0(t3)')
        else:
            gen.add_lw('t2', str(endFor.value))


        gen.add_slt('t0', 't1', 't2')
        gen.add_beqz('t0', lvlExitBucle)
        
        
        for inst in self.InstFor:
            res = inst.ejecutar(ast, for_env, gen, lvlExitBucle, lvlcontinue, lvlreturno)
        

        

        gen.new_body_label(lvlcontinue)

        if devuelto.isTemp:
            if 't' in str(devuelto.value):
                gen.add_move('t3', str(devuelto.value))
            else:
                gen.add_li('t3', str(devuelto.value))
            #gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
        else:
            gen.add_lw('t1', str(devuelto.value))


        gen.add_li('t3', str(temp))
        gen.add_lw('t2', '0(t3)')
        

        gen.add_operation('add', 't0', 't1', 't2')
        gen.add_la('t1', str(devuelto.value))
        gen.add_sw('t0', '0(t1)')

        gen.add_jump(lvlInitBucle)

        gen.new_body_label(lvlExitBucle)

        # devuelto.value = devuelto.value + 1
        # dicciSym = {}
        # dicciSym["const"] = devuelto
        # for_env.setVariable(devuelto.line, devuelto.col, ast, self.IDFirst, dicciSym)
        
        return None


            



        


        
        