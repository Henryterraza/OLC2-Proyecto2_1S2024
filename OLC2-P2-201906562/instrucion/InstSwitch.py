from interface.instruccion import Instruction
from instrucion.SwitchDefault import SwitchDef
from instrucion.SwitchCase import SwitchCase
from environment.environment import Environment
from environment.types import Type
from environment.generator import Generator
from environment.value import Value


# from expressions.continue_statement import Continue

class Switch(Instruction):
    def __init__(self, line, col, exp, listCase):
        self.line = line
        self.col = col
        self.exp = exp
        self.listCase = listCase

    def ejecutar(self, ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):
        
       

        # switch_env = Environment(env, "SWITCH")

        # DefaultCorrect = True

        # for i, case in enumerate(self.listCase):
        #     if isinstance(case, SwitchDef):
        #         if i + 1 != len(self.listCase):
        #             DefaultCorrect = False
        #             break

        # if not DefaultCorrect:
        #     list = ["La clausula default debe ir al final del switch", switch_env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        # existBreak = True

        # for case in self.listCase:  
        #     if isinstance(case, SwitchCase):
        #         resp = case.GetExpresion(ast, switch_env)

        #         if resp.value == validate.value or (not existBreak):
        #             res = case.ejecutar(ast, switch_env)
        #             if res != None:
        #                 if  res.type == Type.BREAK :
        #                     return None
        #                 elif res.type == Type.CONTINUE or res.type == Type.RETURN:
        #                     return res 
        #             existBreak = False
        #     else:
        #         res = case.ejecutar(ast, switch_env)
        #         if res != None:
        #             if  res.type == Type.BREAK :
        #                 return None
        #             elif res.type == Type.CONTINUE or res.type == Type.RETURN:
        #                 return res

        # return None

        # Obtener simbolo
       
        gen.comment("Sentencia Switch")
        switch_env = Environment(env, "SWITCH")

        DefaultCorrect = True

        for i, case in enumerate(self.listCase):
            if isinstance(case, SwitchDef):
                if i + 1 != len(self.listCase):
                    DefaultCorrect = False
                    break

        if not DefaultCorrect:
            list = ["La clausula default debe ir al final del switch", switch_env.id, self.line, self.col, "Semantico"]
            ast.setErrors(list)
            return

        


        existBreak = True

        labelSali = gen.new_label()
        

        retorno = None

        Expresion = self.exp.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)

        for case in self.listCase:  
            label2 = gen.new_label()

            if isinstance(case, SwitchCase):
                resp = case.GetExpresion(ast, switch_env, gen, lvlbreak, lvlcont, lvlreturno)
               

                if resp.type == Expresion.type:
                    if resp.type == Type.INTEGER:
                        if Expresion.isTemp:
                            if 't' in str(Expresion.value):
                                gen.add_move('t3', str(Expresion.value))
                            else:
                                gen.add_li('t3', str(Expresion.value))
                            #gen.add_li('t3', str(Expresion.value))
                            gen.add_lw('t1', '0(t3)')
                        else:
                            gen.add_lw('t1', str(Expresion.value))

                        if resp.isTemp:

                            if 't' in str(resp.value):
                                gen.add_move('t3', str(resp.value))
                            else:
                                gen.add_li('t3', str(resp.value))
                            gen.add_lw('t2', '0(t3)')
                        else:
                            gen.add_lw('t2', str(resp.value))


                        
                        gen.add_bne('t1', 't2', label2 )

                    if resp.type == Type.FLOAT:
                        gen.add_flw('f1', str(Expresion.value))

                        gen.add_flw('f2', str(resp.value))

                        gen.add_feqs('t0', 'f1', 'f2' )



                    
                    if resp.type == Type.BOOLEAN:
                        if Expresion.isTemp:
                            if 't' in str(Expresion.value):
                                gen.add_move('t3', str(Expresion.value))
                            else:
                                gen.add_li('t3', str(Expresion.value))
                            #gen.add_li('t3', str(Expresion.value))
                            gen.add_lw('t1', '0(t3)')
                        else:
                            gen.add_lw('t1', str(Expresion.value))

                        if resp.isTemp:

                            if 't' in str(resp.value):
                                gen.add_move('t3', str(resp.value))
                            else:
                                gen.add_li('t3', str(resp.value))
                            gen.add_lw('t2', '0(t3)')
                        else:
                            gen.add_lw('t2', str(resp.value))


                    res = case.ejecutar(ast, switch_env, gen, labelSali, lvlcont, lvlreturno)
                        
                    existBreak = False

                    gen.new_body_label(label2)

            else:
                res = case.ejecutar(ast, switch_env, gen, labelSali, lvlcont, lvlreturno)

        gen.new_body_label(labelSali)

        return retorno