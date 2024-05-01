from interface.instruccion import Instruction
from environment.types import Type
from environment.generator import Generator

class OutConsole(Instruction):
    def __init__(self, line, col, Exp):
        self.line = line
        self.col = col
        self.Exp = Exp

    def ejecutar(self, ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):
        # outText = ""
        # for exp in self.Exp:
        #     sym = exp.ejecutar(ast, env)
        #     if sym.type == Type.ARRAY:
        #         outText += "["
        #         val = ""
        #         try:
        #             val = sym.value.value
        #         except:
        #             val = sym.value


        #         for arr in val:
        #             outText += " " + str(arr.value) + ", "
        #         outText += "]"
        #     else:
        #         outText += str(sym.value) + " "
        # ast.setConsole(outText)
        for exp in self.Exp:
            val = exp.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
            print(val.value)
            gen.comment('Impriendo el valor')
            if (val.type == Type.INTEGER):
                # Imprimiendo expresion
                gen.add_br()
                if val.isTemp:
                    if 't' in str(val.value):
                        gen.add_move('t3', str(val.value))
                    else:
                        gen.add_li('t3', str(val.value))
                    gen.add_lw('a0', '0(t3)')
                else:
                    gen.add_lw('a0', val.value)
                
                gen.add_li('a7', '1')
                gen.add_system_call()
            elif (val.type == Type.STRING):
                gen.add_br()
                if 't' in str(val.value) and len(str(val.value)) < 2:
                    gen.add_move('a0', str(val.value))
                else:
                    gen.add_la('a0', str(val.value))
                gen.add_li('a7', '4')
                gen.add_system_call()
            elif (val.type == Type.FLOAT):
                gen.add_br()
                # if 't' in str(val.value):
                #     gen.add_move('a0', str(val.value))
                # else:
                #     gen.add_la('a0', str(val.value))
                # gen.add_li('a7', '4')
                # gen.add_system_call()

                gen.add_flw('fa0', val.value)
                gen.add_li('a7', '2')
                gen.add_system_call()
            elif (val.type == Type.BOOLEAN):
                gen.add_br()
                if val.isTemp:
                    if 't' in str(val.value):
                        gen.add_move('t3', str(val.value))
                    else:
                        gen.add_li('t3', str(val.value))
                    gen.add_lw('a0', '0(t3)')
                else:
                    gen.add_lw('a0', val.value)
                newLabel = gen.new_label()
                gen.add_beqz('a0', newLabel)
                gen.add_la('a0', 'msg_true')
                gen.add_li('a7', '4')
                gen.add_system_call()
                newLabel2 = gen.new_label()
                gen.add_jump(newLabel2)

                gen.new_body_label(newLabel)
                gen.add_la('a0', 'msg_false')
                gen.add_li('a7', '4')
                gen.add_system_call()
                gen.new_body_label(newLabel2)
            elif (val.type == Type.NULL):
                gen.add_br()
                if 't' in str(val.value) and len(str(val.value)) < 2:
                    gen.add_move('a0', str(val.value))
                else:
                    gen.add_la('a0', str(val.value))
                gen.add_li('a7', '4')
                gen.add_system_call()


        gen.comment('Salto de linea')
        gen.add_br()
        gen.add_li('a0', '10')
        gen.add_li('a7', '11')
        gen.add_system_call()

        return None

    # def PrintMatrix(self, array, outvalue):
    #     for arr in array:
    #         if arr == Type.ARRAY:
    #             return self.PrintMatrix(arr, outvalue)
    #         else:
    #             outvalue += str(arr)
    #     return outvalue