from interface.instruccion import Instruction
from environment.value import Value
from environment.generator import Generator
from environment.environment import Environment
from environment.types import Type, Reser_Words, StringType


class Declaration(Instruction):
    def __init__(self, line,  col, TipoDec, id, type, exp):
        self.line = line
        self.col = col
        self.TipoDec = TipoDec
        self.id = id
        self.type = type
        self.exp = exp

    def ejecutar(self, ast, env: Environment, gen: Generator, lvlbreak, lvlcont, lvlreturno):

        # if Reser_Words.Verificar(self.id):
        #     list = ["El id ya existe como palabra reservada", env.id, self.line, self.col, "Semantico"]
        #     ast.setErrors(list)
        #     return

        # # Validar tipo
        # if self.exp != None and self.type != None :
        #      # Obtener simbolo
        #     result = self.exp.ejecutar(ast, env)

        #     if self.type == Type.FLOAT and result.type == Type.INTEGER:
        #         result.value = float(result.value)
        #     elif result.type != self.type:
        #         list = ["Los tipos de dato son incorrectos", env.id, self.line, self.col, "Semantico"]
        #         ast.setErrors(list)
        #         return
        # elif self.exp == None and self.type != None:
        #     if self.TipoDec == "var":
        #         if self.type == Type.INTEGER:
        #             result = Symbol(self.line, self.col, 0, Type.INTEGER)
        #         elif self.type == Type.FLOAT:
        #             result = Symbol(self.line, self.col, 0.0, Type.FLOAT)
        #         elif self.type == Type.STRING:
        #             result = Symbol(self.line, self.col, "", Type.STRING)
        #         elif self.type == Type.CHAR:
        #             result = Symbol(self.line, self.col, '', Type.CHAR)
        #         elif self.type == Type.BOOLEAN:
        #             result = Symbol(self.line, self.col, True, Type.BOOLEAN)
        #     else:
        #         list = [f"La constante {id} debe tener un valor asignado", env.id, self.line, self.col, "Semantico"]
        #         ast.setErrors(list)
        #         return
        # elif self.exp != None and self.type == None:
        #      # Obtener simbolo
        #     result = self.exp.ejecutar(ast, env)

        #     self.type = result.type


        # contenido = {}

        # contenido[self.TipoDec] = result 
   
        #  # Agregar al entorno
        # TipSimb = ""
        # if self.TipoDec == "var":
        #     TipSimb = "variable"
        # else:
        #     TipSimb = "constante"

        # list = [self.id,  TipSimb, StringType.Retorno(result.type.value) , env.id, self.line, self.col]
        # ast.setsimbols(list)
        # env.saveVariable(self.line, self.col, ast, self.id, contenido)
        
        newvariable = Value(str(self.id), False, Type.INTEGER, [],[],[])


        if self.exp != None and self.type != None :
             # Obtener simbolo
            result = self.exp.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
            
            if self.type == Type.FLOAT and result.type == Type.INTEGER:
                if 't' in str(result.value):
                    gen.add_move('t3', str(result.value))
                else:
                    gen.add_li('t3', str(result.value))
                #gen.add_li('t3', str(op1.value))
                gen.add_lw('t1', '0(t3)')
                gen.comment('Conversion de entero a flotante')
                gen.add_fcvtsw('f0', 't1')
                gen.variable_data(str(self.id), 'float', '0.0')
                gen.variable_data(str(self.id) + '.typeof', 'string', '\"float\"')

                gen.add_fsw('f0', str(self.id))

                newvariable.type = Type.FLOAT


                # result.value = float(result.value)
            elif result.type != self.type:
                list = ["Los tipos de dato son incorrectos", env.id, self.line, self.col, "Semantico"]
                ast.setErrors(list)
                return None
            

            if result.type == Type.INTEGER:
                gen.variable_data(str(self.id), 'word', '0')
                gen.variable_data(str(self.id) + '.typeof', 'string', '\"number\"')

                if 't' in str(result.value):
                    gen.add_move('t3', str(result.value))
                else:
                    gen.add_li('t3', str(result.value))
                #gen.add_li('t3', str(op1.value))
                gen.add_lw('t1', '0(t3)')
                gen.add_la('t0', str(self.id))
                gen.add_sw('t1', '0(t0)')

                newvariable.type = Type.INTEGER

                # result = Symbol(self.line, self.col, 0, Type.INTEGER)
            elif result.type == Type.FLOAT:
                gen.variable_data(str(self.id), 'float', '0.0')
                gen.variable_data(str(self.id) + '.typeof', 'string', '\"float\"')

                gen.comment('Optenr float y guardarlo en otra direccion')
                gen.add_flw('f0', str(result.value) )
                gen.add_fsw('f0', str(self.id))

                newvariable.type = Type.FLOAT

                # result = Symbol(self.line, self.col, 0.0, Type.FLOAT)
            elif result.type == Type.STRING:
                gen.variable_data(str(self.id), 'space', '70')
                gen.variable_data(str(self.id) + '.typeof', 'string', '\"string\"')

                newLabel1 = gen.new_label()
                gen.add_la('t0', str(result.value))
                gen.add_la('t1', str(self.id))
                
                gen.new_body_label(newLabel1)
                
                gen.add_lb('t3', '0(t0)')
                gen.add_sb('t3', '0(t1)')

                gen.add_addi('t0', 't0', '1')
                gen.add_addi('t1', 't1', '1')
                
                newLabel2 = gen.new_label()
                gen.add_beqz('t3', newLabel2)
                
                gen.add_jump(newLabel1)
                gen.new_body_label(newLabel2)

                newvariable.type = Type.STRING

                
                # result = Symbol(self.line, self.col, "", Type.STRING)
            # elif self.type == Type.CHAR:
            #     result = Symbol(self.line, self.col, '', Type.CHAR)
            elif result.type == Type.BOOLEAN:
                gen.variable_data(str(self.id), 'word', '1')
                gen.variable_data(str(self.id) + '.typeof', 'string', '\"boolean\"')
                
                
                gen.comment('se asigna el valor a la variable')
                if 't' in str(result.value):
                    gen.add_move('t3', str(result.value))
                else:
                    gen.add_li('t3', str(result.value))
                #gen.add_li('t3', str(op1.value))
                gen.add_lw('t1', '0(t3)')
                gen.add_la('t0', str(self.id))
                gen.add_sw('t1', '0(t0)')

                newvariable.type = Type.BOOLEAN



                # result = Symbol(self.line, self.col, True, Type.BOOLEAN)

            
            




            
        elif self.exp == None and self.type != None:
            if self.TipoDec == "var":
                if self.type == Type.INTEGER:
                    gen.variable_data(str(self.id), 'word', '0')
                    gen.variable_data(str(self.id) + '.typeof', 'string', '\"number\"')

                    newvariable.type = Type.INTEGER
                    # result = Symbol(self.line, self.col, 0, Type.INTEGER)
                elif self.type == Type.FLOAT:
                    gen.variable_data(str(self.id), 'float', '0.0')
                    gen.variable_data(str(self.id) + '.typeof', 'string', '\"float\"')

                    newvariable.type = Type.FLOAT
                    # result = Symbol(self.line, self.col, 0.0, Type.FLOAT)
                elif self.type == Type.STRING:
                    gen.variable_data(str(self.id), 'asciz', '70')
                    gen.variable_data(str(self.id) + '.typeof', 'string', '\"string\"')
                    # result = Symbol(self.line, self.col, "", Type.STRING)
                # elif self.type == Type.CHAR:
                #     result = Symbol(self.line, self.col, '', Type.CHAR)
                    newvariable.type = Type.STRING

                elif self.type == Type.BOOLEAN:
                    gen.variable_data(str(self.id), 'word', '1')
                    gen.variable_data(str(self.id) + '.typeof', 'string', '\"boolean\"')
                    
                    newvariable.type = Type.BOOLEAN
                    # result = Symbol(self.line, self.col, True, Type.BOOLEAN)
            else:
                list = [f"La constante {self.id} debe tener un valor asignado", env.id, self.line, self.col, "Semantico"]
                ast.setErrors(list)
                return
        elif self.exp != None and self.type == None:
             # Obtener simbolo
            result = self.exp.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
            if result.type == Type.INTEGER:
                gen.variable_data(str(self.id), 'word', '0')
                gen.variable_data(str(self.id) + '.typeof', 'string', '\"number\"')

                if 't' in str(result.value):
                    gen.add_move('t3', str(result.value))
                else:
                    gen.add_li('t3', str(result.value))
                #gen.add_li('t3', str(op1.value))
                gen.add_lw('t1', '0(t3)')
                gen.add_la('t0', str(self.id))
                gen.add_sw('t1', '0(t0)')

                newvariable.type = Type.INTEGER

                # result = Symbol(self.line, self.col, 0, Type.INTEGER)
            elif result.type == Type.FLOAT:
                gen.variable_data(str(self.id), 'float', '0.0')
                gen.variable_data(str(self.id) + '.typeof', 'string', '\"float\"')

                gen.comment('Optenr float y guardarlo en otra direccion')
                gen.add_flw('f0', str(result.value) )
                gen.add_fsw('f0', str(self.id))

                newvariable.type = Type.FLOAT

                # result = Symbol(self.line, self.col, 0.0, Type.FLOAT)
            elif result.type == Type.STRING:
                gen.variable_data(str(self.id), 'space', '70')
                gen.variable_data(str(self.id) + '.typeof', 'string', '\"string\"')

                newLabel1 = gen.new_label()
                gen.add_la('t0', str(result.value))
                gen.add_la('t1', str(self.id))
                
                gen.new_body_label(newLabel1)
                
                gen.add_lb('t3', '0(t0)')
                gen.add_sb('t3', '0(t1)')

                gen.add_addi('t0', 't0', '1')
                gen.add_addi('t1', 't1', '1')
                
                newLabel2 = gen.new_label()
                gen.add_beqz('t3', newLabel2)
                
                gen.add_jump(newLabel1)
                gen.new_body_label(newLabel2)

                newvariable.type = Type.STRING

                
                # result = Symbol(self.line, self.col, "", Type.STRING)
            # elif self.type == Type.CHAR:
            #     result = Symbol(self.line, self.col, '', Type.CHAR)
            elif result.type == Type.BOOLEAN:
                gen.variable_data(str(self.id), 'word', '1')
                gen.variable_data(str(self.id) + '.typeof', 'string', '\"boolean\"')
                
                
                gen.comment('se asigna el valor a la variable')
                if 't' in str(result.value):
                    gen.add_move('t3', str(result.value))
                else:
                    gen.add_li('t3', str(result.value))
                #gen.add_li('t3', str(op1.value))
                gen.add_lw('t1', '0(t3)')
                gen.add_la('t0', str(self.id))
                gen.add_sw('t1', '0(t0)')

                newvariable.type = Type.BOOLEAN



                # result = Symbol(self.line, self.col, True, Type.BOOLEAN)





        contenido = {}

        contenido[self.TipoDec] = newvariable 
   
         # Agregar al entorno
        TipSimb = ""
        if self.TipoDec == "var":
            TipSimb = "variable"
        else:
            TipSimb = "constante"

        list = [self.id,  TipSimb, StringType.Retorno(newvariable.type.value) , env.id, self.line, self.col]
        ast.setsimbols(list)
        env.saveVariable(self.line, self.col, ast, self.id, contenido)


        return None
