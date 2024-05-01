from interface.expression import Expression
from environment.types import TypeCond, Type
from environment.value import Value
from environment.generator import Generator

class OperRelac(Expression):
    def __init__(self, line, col, OpLeft,OpRight, OpRelac):
        self.line = line
        self.col = col
        self.OpLeft = OpLeft
        self.OpRight = OpRight
        self.OpRelac  = OpRelac

    def ejecutar(self, ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):
        
        OpL = self.OpLeft.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
        OpR = self.OpRight.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)

        temp = gen.new_temp()

        gen.comment('Agregando valor booleano')



        # falta verificar si es valor izquierdo es flotante y si el derecho es entero o viseversa para realizar la conversion a flotantes y verificar su relacion
        # eh ira aqui la comparacion para luego entrar en la configuracion
        if OpL.type == OpR.type:

            if OpL.type != Type.STRING and OpL.type != Type.NULL :

                if OpL.type == Type.INTEGER:
                    if OpL.isTemp:

                        if 't' in str(OpL.value):
                            gen.add_move('t3', str(OpL.value))
                        else:
                            gen.add_li('t3', str(OpL.value))
                        #gen.add_li('t3', str(OpL.value))
                        gen.add_lw('t1', '0(t3)')
                    else:
                        gen.add_lw('t1', str(OpL.value))
                    
                    if OpR.isTemp:
                        if 't' in str(OpR.value):
                            gen.add_move('t3', str(OpR.value))
                        else:
                            gen.add_li('t3', str(OpR.value)) 
                        #gen.add_li('t3', str(OpR.value))
                        gen.add_lw('t2', '0(t3)')
                    else:
                        gen.add_lw('t2', str(OpR.value))

                if OpL.type == Type.FLOAT:
                        gen.add_flw('f0', str(OpL.value))
                        gen.add_flw('f1', str(OpR.value))


                labe1l = gen.new_label()
                gen.add_br()
                label2 = gen.new_label()


                if self.OpRelac == TypeCond.EQUAL:
                    gen.comment('Se verifica si es igual')
                    if OpL.type == Type.INTEGER:
                        
                        gen.add_beq('t1', 't2', labe1l)

                        gen.add_li('t0', '0')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')

                        gen.add_jump(label2)

                        gen.new_body_label(labe1l)
                        gen.add_li('t0', '1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        gen.new_body_label(label2)
                    elif OpL.type == Type.FLOAT:

                        gen.add_feqs('t0', 'f0', 'f1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')


                    return Value(str(temp), True, Type.BOOLEAN, [], [], [])

                elif  self.OpRelac == TypeCond.DIF:
                    gen.comment('Se verifica si no es igual')
                    if OpL.type == Type.INTEGER:
                        
                        
                        gen.add_bne('t1', 't2', labe1l)

                        gen.add_li('t0', '0')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')

                        gen.add_jump(label2)

                        gen.new_body_label(labe1l)
                        gen.add_li('t0', '1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        gen.new_body_label(label2)
                    elif OpL.type == Type.FLOAT:
                        
                        gen.add_feqs('t0', 'f0', 'f1')
                        gen.add_beqz('t0', labe1l)
                        gen.add_li('t0', '0')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')

                        gen.add_jump(label2)

                        gen.new_body_label(labe1l)
                        gen.add_li('t0', '1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        gen.new_body_label(label2)
                    return Value(str(temp), True, Type.BOOLEAN, [], [], [])

                elif  self.OpRelac == TypeCond.MAY:
                    
                    if OpL.type == Type.INTEGER:
                        
                        gen.comment('Se verifica si es mayor')
                        gen.add_bgt('t1', 't2', labe1l)

                        gen.add_li('t0', '0')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')

                        gen.add_jump(label2)

                        gen.new_body_label(labe1l)
                        gen.add_li('t0', '1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        gen.new_body_label(label2)
                    elif OpL.type == Type.FLOAT:
                        gen.comment('Se verifica si es mayor')
                        gen.add_fgts('t0', 'f0', 'f1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')


                    return Value(str(temp), True, Type.BOOLEAN, [], [], [])



                elif  self.OpRelac == TypeCond.MAYEQ:
                    if OpL.type == Type.INTEGER:
                        
                        gen.comment('Se verifica si es mayor o igual')
                        gen.add_bge('t1', 't2', labe1l)

                        gen.add_li('t0', '0')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')

                        gen.add_jump(label2)

                        gen.new_body_label(labe1l)
                        gen.add_li('t0', '1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        gen.new_body_label(label2)
                    elif OpL.type == Type.FLOAT:
                        gen.comment('Se verifica si es mayor')
                        gen.add_fges('t0', 'f0', 'f1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')


                    return Value(str(temp), True, Type.BOOLEAN, [], [], [])

                elif  self.OpRelac == TypeCond.MEN:
                    if OpL.type == Type.INTEGER:
                        
                        gen.comment('Se verifica si es menor')
                        gen.add_blt('t1', 't2', labe1l)

                        gen.add_li('t0', '0')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')

                        gen.add_jump(label2)

                        gen.new_body_label(labe1l)
                        gen.add_li('t0', '1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        gen.new_body_label(label2)
                    elif OpL.type == Type.FLOAT:
                        gen.comment('Se verifica si es mayor')
                        gen.add_flts('t0', 'f0', 'f1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')


                    return Value(str(temp), True, Type.BOOLEAN, [], [], [])

                elif  self.OpRelac == TypeCond.MENEQ:
                    if OpL.type == Type.INTEGER:
                        
                        gen.comment('Se verifica si es menoro igual')
                        gen.add_ble('t1', 't2', labe1l)

                        gen.add_li('t0', '0')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')

                        gen.add_jump(label2)

                        gen.new_body_label(labe1l)
                        gen.add_li('t0', '1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        gen.new_body_label(label2)
                    elif OpL.type == Type.FLOAT:
                        gen.comment('Se verifica si es mayor')
                        gen.add_fles('t0', 'f0', 'f1')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')


                    return Value(str(temp), True, Type.BOOLEAN, [], [], [])

                # else:
                #     return Symbol(self.line, self.col, None, Type.NULL)
            
            
        gen.add_li('t0', '0')
        gen.add_li('t3', str(temp))
        gen.add_sw('t0', '0(t3)')

        return Value(str(temp), True, Type.BOOLEAN, [], [], [])
            

        
       