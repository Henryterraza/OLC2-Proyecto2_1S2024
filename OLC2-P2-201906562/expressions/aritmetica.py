from interface.expression import Expression
from environment.symbol import Symbol
from environment.types import TypeAritmetica, Type, StringType
from environment.TablesDominacion import dominant_tableSum, dominant_tableRestDivMult, dominant_tableModulo
from environment.ast import Ast
from environment.value import Value
from environment.generator import Generator



class Aritmetica(Expression):
    def __init__(self, line, col, OpLeft, OpRight, operador):
        self.line = line
        self.col = col
        self.OpLeft = OpLeft
        self.OpRight = OpRight
        self.operador: TypeAritmetica = operador

    def ejecutar(self, ast:Ast, env, gen: Generator, lvlbreak, lvlcont, lvlreturno):

        # OpL:Symbol =  self.OpLeft.ejecutar(ast, env)
        # OpR:Symbol =  self.OpRight.ejecutar(ast, env)
        # Errores = []

        # if OpL.value != None and OpR.value != None:
        #     if self.Operador == TypeAritmetica.SUMA:
        #         TipoDominant = dominant_tableSum[OpL.type.value][OpR.type.value]
        #         if TipoDominant == Type.INTEGER:
        #             return Symbol(line=self.line, col=self.col, value=OpL.value + OpR.value, type=Type.INTEGER)
        #         elif TipoDominant == Type.FLOAT:
        #             return Symbol(line=self.line, col=self.col, value=OpL.value + OpR.value, type=Type.FLOAT)
        #         elif TipoDominant == Type.STRING:
        #             return Symbol(line=self.line, col=self.col, value=OpL.value + OpR.value, type=Type.STRING)
        #         else:
        #             list = [f"La suma de un " + StringType.Retorno(OpL.type.value) + " y " + StringType.Retorno(OpR.type.value) + " no se puede", env.id, self.line, self.col, "Semantico"]
        #             ast.setErrors(list)

        #             return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        #     elif self.Operador == TypeAritmetica.RESTA:
        #         TipoDominant = dominant_tableRestDivMult[OpL.type.value][OpR.type.value]
        #         if TipoDominant == Type.INTEGER:
        #             return Symbol(line=self.line, col=self.col, value=OpL.value - OpR.value, type=Type.INTEGER)
        #         elif TipoDominant == Type.FLOAT:
        #             return Symbol(line=self.line, col=self.col, value=OpL.value - OpR.value, type=Type.FLOAT)
        #         else:
                    
        #             list = [f"La resta de un " + StringType.Retorno(OpL.type.value) + " y " + StringType.Retorno(OpR.type.value) + " no se puede", env.id, self.line, self.col, "Semantico"]
        #             ast.setErrors(list)

        #             return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        #     elif self.Operador == TypeAritmetica.DIV:
        #         TipoDominant = dominant_tableRestDivMult[OpL.type.value][OpR.type.value]
        #         if float(OpR.value) != 0.0: 
        #             if TipoDominant == Type.INTEGER:
        #                 return Symbol(line=self.line, col=self.col, value=OpL.value / OpR.value, type=Type.INTEGER)
        #             elif TipoDominant == Type.FLOAT:
        #                 return Symbol(line=self.line, col=self.col, value=OpL.value / OpR.value, type=Type.FLOAT)
        #             else:
        #                 list = [f"La Div de un " + StringType.Retorno(OpL.type.value) + " y " + StringType.Retorno(OpR.type.value) + " no se puede", env.id, self.line, self.col, "Semantico"]
        #                 ast.setErrors(list)

        #                 return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        #         else:
        #             list = [f"No se puede dividir entre 0", env.id, self.line, self.col, "Semantico"]
        #             ast.setErrors(list)

        #             return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        #     elif self.Operador == TypeAritmetica.MULT:
        #         TipoDominant = dominant_tableRestDivMult[OpL.type.value][OpR.type.value]
        #         if TipoDominant == Type.INTEGER:
        #             return Symbol(line=self.line, col=self.col, value=OpL.value * OpR.value, type=Type.INTEGER)
        #         elif TipoDominant == Type.FLOAT:
        #             return Symbol(line=self.line, col=self.col, value=OpL.value * OpR.value, type=Type.FLOAT)
        #         else:
        #             list = [f"La multiplicacion de un " + StringType.Retorno(OpL.type.value) + " y " + StringType.Retorno(OpR.type.value) + " no se puede", env.id, self.line, self.col, "Semantico"]
        #             ast.setErrors(list)

        #             return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        #     elif self.Operador == TypeAritmetica.MOD:
        #         TipoDominant = dominant_tableModulo[OpL.type.value][OpR.type.value]
        #         if OpR.value != 0: 
        #             if TipoDominant == Type.INTEGER:
        #                 return Symbol(line=self.line, col=self.col, value=OpL.value % OpR.value, type=Type.INTEGER)
        #             else:
        #                 list = [f"El mod de un " + StringType.Retorno(OpL.type.value) + " y " + StringType.Retorno(OpR.type.value) + " no se puede", env.id, self.line, self.col, "Semantico"]
        #                 ast.setErrors(list)

        #                 return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
        #         else:
        #             list = [f"El modulo de un numero entre 0 no se puede", env.id, self.line, self.col, "Semantico"]
        #             ast.setErrors(list)

        #             return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)
                
        #     elif self.Operador == TypeAritmetica.UMENOS:
        #         if OpL.type == Type.INTEGER:
        #             return Symbol(line=self.line, col=self.col, value=-OpL.value, type=Type.INTEGER)
        #         elif OpL.type == Type.FLOAT:
        #             return Symbol(line=self.line, col=self.col, value=-OpL.value, type=Type.FLOAT)
        #         else:
        #             list = [f"La negacion de un " + StringType.Retorno(OpL.type.value) + "no se puede", env.id, self.line, self.col, "Semantico"]
        #             ast.setErrors(list)
                   
        #             return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)


        # return Symbol(line=self.line, col=self.col, value=None, type=Type.NULL)

         # Ejecución de operandos
        op1 = self.OpLeft.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
        op2 = self.OpRight.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)

        if op1.value != None and op2.value != None:
            gen.add_br()
            gen.comment('Realizando operacion')

            TipoDominant = dominant_tableSum[op1.type.value][op2.type.value]
            if TipoDominant != Type.NULL:
                if TipoDominant == Type.INTEGER:
                    if op1.isTemp:

                        if 't' in str(op1.value):
                            gen.add_move('t3', str(op1.value))
                        else:
                            gen.add_li('t3', str(op1.value))
                        #gen.add_li('t3', str(op1.value))
                        gen.add_lw('t1', '0(t3)')
                    else:
                        gen.add_lw('t1', str(op1.value))
                    
                    if op2.isTemp:
                        if 't' in str(op2.value):
                            gen.add_move('t3', str(op2.value))
                        else:
                            gen.add_li('t3', str(op2.value)) 
                        #gen.add_li('t3', str(op2.value))
                        gen.add_lw('t2', '0(t3)')
                    else:
                        gen.add_lw('t2', str(op2.value))

                    temp = gen.new_temp()
                elif TipoDominant == Type.FLOAT:

                    if op1.type == Type.FLOAT and op2.type == Type.FLOAT:
                        gen.add_flw('f0', str(op1.value))
                        gen.add_flw('f1', str(op2.value))

                    elif op1.type == Type.INTEGER and op2.type == Type.FLOAT:
                        if op1.isTemp:
                            if 't' in str(op1.value):
                                gen.add_move('t3', str(op1.value))
                            else:
                                gen.add_li('t3', str(op1.value))
                            #gen.add_li('t3', str(op1.value))
                            gen.add_lw('t1', '0(t3)')
                        else:
                            gen.add_lw('t1', op1.value)

                        gen.comment('Conversion de entero a flotante')
                        gen.add_fcvtsw('f0', 't1')
                        gen.add_flw('f1', str(op2.value))
                    elif op1.type == Type.FLOAT and op2.type == Type.INTEGER:
                        if op2.isTemp:
                            if 't' in str(op2.value):
                                gen.add_move('t3', str(op2.value))
                            else:
                                gen.add_li('t3', str(op2.value))
                            #gen.add_li('t3', str(op1.value))
                            gen.add_lw('t1', '0(t3)')
                        else:
                            gen.add_lw('t1', op2.value)

                        gen.comment('Conversion de entero a flotante')
                        gen.add_fcvtsw('f1', 't1')
                        gen.add_flw('f0', str(op1.value))

                    
                    tempFloat = gen.new_float()
                    nameId = 'Flt_'+str(tempFloat)
                    nameIdType = 'Flt_'+str(tempFloat) +'.typeof'
                    gen.variable_data(nameId, 'float', str(0.0))
                    gen.variable_data(nameIdType, 'string', '\"float\"')





                if self.operador == TypeAritmetica.SUMA:
                    if TipoDominant == Type.INTEGER:
                        gen.add_operation('add', 't0', 't1', 't2')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        return  Value(str(temp), True, Type.INTEGER, [], [], [])
                    if TipoDominant == Type.FLOAT:
                        gen.add_operation('fadd.s', 'f2', 'f0', 'f1')
                        gen.add_fsw('f2', str(nameId))
                        return  Value(nameId, False, Type.FLOAT, [], [], [])
            
                if self.operador == TypeAritmetica.RESTA:
                    if TipoDominant == Type.INTEGER:
                        gen.add_operation('sub', 't0', 't1', 't2')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        return  Value(str(temp), True, Type.INTEGER, [], [], [])
                    if TipoDominant == Type.FLOAT:
                        gen.add_operation('fsub.s', 'f2', 'f0', 'f1')
                        gen.add_fsw('f2', str(nameId))
                        return  Value(nameId, False, Type.FLOAT, [], [], [])

                
                if self.operador == TypeAritmetica.MULT:
                    if TipoDominant == Type.INTEGER:
                        gen.add_operation('mul', 't0', 't1', 't2')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')

                        return  Value(str(temp), True, Type.INTEGER, [], [], [])
                    if TipoDominant == Type.FLOAT:
                        gen.add_operation('fmul.s', 'f2', 'f0', 'f1')
                        gen.add_fsw('f2', str(nameId))
                        return  Value(nameId, False, Type.FLOAT, [], [], [])


                
                if self.operador == TypeAritmetica.DIV:
                    if TipoDominant == Type.INTEGER:
                        gen.add_operation('div', 't0', 't1', 't2')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')

                        return  Value(str(temp), True, Type.INTEGER, [], [], [])
                    if TipoDominant == Type.FLOAT:
                        gen.add_operation('fdiv.s', 'f2', 'f0', 'f1')
                        gen.add_fsw('f2', str(nameId))
                        return  Value(nameId, False, Type.FLOAT, [], [], [])
                
               

        
        return Value('msg_null', False, Type.NULL, [], [], [])