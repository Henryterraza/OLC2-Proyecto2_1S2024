from interface.expression import Expression
from environment.types import TypeCond, Type, StringType
from environment.value import Value
from environment.generator import Generator

class OperCond(Expression):
    def __init__(self, line, col, OpLeft,OpRight, OpCond):
        self.line = line
        self.col = col
        self.OpLeft = OpLeft
        self.OpRight = OpRight
        self.OpCond  = OpCond

    def ejecutar(self, ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):

        


        if self.OpLeft != None and self.OpRight != None:
            OpL = self.OpLeft.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno )
            OpR = self.OpRight.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)



            #cargando lado izquierdo
            gen.add_li('t0', str(OpL.value))
            gen.add_lw('t1', '0(t0)')
            #cargando lado derecho
            gen.add_li('t0', str(OpR.value))
            gen.add_lw('t2', '0(t0)')

            gen.comment('Operacion condicional')

        temp = gen.new_temp()

        if self.OpCond == TypeCond.AND:

            gen.add_and('t0', 't1', 't2')

            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')


            return Value(str(temp), True, Type.BOOLEAN, [], [], [])
        elif  self.OpCond == TypeCond.OR:

            gen.add_or('t0', 't1', 't2')

            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
           
            return Value(str(temp), True, Type.BOOLEAN, [], [], [])
        elif  self.OpCond == TypeCond.NOT:
            OpL = self.OpLeft.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
            if OpL.type == Type.BOOLEAN:
                #cargando lado izquierdo
                if OpL.isTemp:
                    if 't' in str(OpL.value):
                        gen.add_move('t0', str(OpL.value))
                    else:
                        gen.add_li('t0', str(OpL.value))
                    #gen.add_li('t3', str(OpL.value))
                    gen.add_lw('t1', '0(t0)')
                else:
                    gen.add_lw('t1', str(OpL.value))
                    

                gen.comment('Operacion condicional')


                gen.add_seqz('t0', 't1')
                

                gen.add_li('t3', str(temp))
                gen.add_sw('t0', '0(t3)')

                return Value(str(temp), True, Type.BOOLEAN, [], [], [])
            
            
            
            
            list = [f"No se puede usar ! en un tipo {StringType.Retorno(OpL.type.value)}", env.id, self.line, self.col, "Semantico"]
            ast.setErrors(list)
            return Value('msg_null', False, Type.NULL, [], [], [])
        

        gen.add_li('t0', '0')
        gen.add_li('t3', str(temp))
        gen.add_sw('t0', '0(t3)')

        return Value(str(temp), True, Type.BOOLEAN, [], [], [])
        