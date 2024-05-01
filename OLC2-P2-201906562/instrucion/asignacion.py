from interface.instruccion import Instruction
from environment.types import Type,TypeAritmetica
from environment.generator import Generator
from expressions.aritmetica import Aritmetica
from expressions.primitive import Primitive


class Assignment(Instruction):
    def __init__(self, line, col, id, exp, operacion):
        self.line = line
        self.col = col
        self.id = id
        self.exp = exp
        self.operacion = operacion

    def ejecutar(self, ast, env, gen: Generator , lvlbreak, lvlcont, lvlreturno):
        # # Obtener simbolo
        # result = self.exp.ejecutar(ast, env)


        # #Verificar si ya existe en todos los entornos
        # Existid = env.getVariable(self.line, self.col, ast, self.id)

        # if Existid == None:
        #     return

        # contenido = None
        # if "var" in Existid:
        #     contenido = Existid["var"]
            
        #     if contenido.type == Type.FLOAT and result.type == Type.INTEGER:
        #         result.value = float(result.value)
        #         result.type = Type.FLOAT
                
        #     elif contenido.type != result.type:
        #         list = ["Los tipos de dato son incorrectos", env.id, self.line, self.col, "Semantico"]
        #         ast.setErrors(list)
        #         return
            
        #     symL = Primitive(self.line, self.col, contenido.value, contenido.type)
        #     symR = Primitive(self.line, self.col, result.value, result.type)
                    

        #     if self.operacion == TypeAritmetica.SUMA:
        #             result = Aritmetica(self.line, self.col, symL, symR, TypeAritmetica.SUMA).ejecutar(ast, env)
        #     elif self.operacion == TypeAritmetica.RESTA:
        #             result = Aritmetica(self.line, self.col, symL, symR, TypeAritmetica.RESTA).ejecutar(ast, env)
        
        
        #     Existid["var"] = result
        #     env.setVariable(self.line, self.col, ast, self.id, Existid)
        #     return
           

        # list = [f"La constante {id} no se le puede cambiar su valor.", self.id, self.line, self.col, "Semantico"]
        # ast.setErrors(list)


         # Obtener simbolo
        result = self.exp.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)


        #Verificar si ya existe en todos los entornos
        Existid = env.getVariable(self.line, self.col, ast, self.id)

        if Existid == None:
            return

        contenido = None

        if "var" in Existid:
            contenido = Existid["var"]
            if self.operacion == TypeAritmetica.ASIGNACION:
                if contenido.type == Type.FLOAT and result.type == Type.INTEGER:
                    if result.isTemp:
                        if 't' in str(result.value):
                            gen.add_move('t3', str(result.value))
                        else:
                            gen.add_li('t3', str(result.value))
                        #gen.add_li('t3', str(op1.value))
                        gen.add_lw('t1', '0(t3)')
                    else:
                        gen.add_lw('t1', result.value)

                    gen.comment('Conversion de entero a flotante')
                    gen.add_fcvtsw('f0', 't1')
                    gen.add_fsw('f0', str(contenido.value))
                    
                elif contenido.type != result.type:
                    list = ["Los tipos de dato son incorrectos", env.id, self.line, self.col, "Semantico"]
                    ast.setErrors(list)
                    return
                
                if contenido.type == Type.INTEGER and result.type == Type.INTEGER:
                    if contenido.isTemp:

                        if 't' in str(contenido.value):
                            gen.add_move('t3', str(contenido.value))
                        else:
                            gen.add_li('t3', str(contenido.value))
                        #gen.add_li('t3', str(op1.value))
                        gen.add_la('t1', '0(t3)')
                    else:
                        gen.add_la('t1', str(contenido.value))
                    
                    if result.isTemp:
                        if 't' in str(result.value):
                            gen.add_move('t3', str(result.value))
                        else:
                            gen.add_li('t3', str(result.value)) 
                        #gen.add_li('t3', str(op2.value))
                        gen.add_lw('t2', '0(t3)')
                    else:
                        gen.add_lw('t2', str(result.value))

                    gen.add_sw('t2', '0(t1)')
                elif contenido.type == Type.FLOAT and result.type == Type.FLOAT:
                    gen.add_flw('f1', str(result.value))
                    gen.comment('se asigna el valor flotante a la varible')
                    gen.add_fsw('f1', str(contenido.value))
                elif contenido.type == Type.STRING and result.type == Type.STRING:
                    gen.add_la('t0', str(result.value))
                    gen.add_la('t1', str(contenido.value))
                    gen.comment('se asigna el valor string a la variable')
                    newLabel1 = gen.new_label()
                    gen.new_body_label(newLabel1)
                
                    gen.add_lb('t3', '0(t0)')
                    gen.add_sb('t3', '0(t1)')

                    gen.add_addi('t0', 't0', '1')
                    gen.add_addi('t1', 't1', '1')
                    
                    newLabel2 = gen.new_label()
                    gen.add_beqz('t3', newLabel2)
                    
                    gen.add_jump(newLabel1)
                    gen.new_body_label(newLabel2)

                elif contenido.type == Type.BOOLEAN and result.type == Type.BOOLEAN:
                    if contenido.isTemp:

                        if 't' in str(contenido.value):
                            gen.add_move('t3', str(contenido.value))
                        else:
                            gen.add_li('t3', str(contenido.value))
                        #gen.add_li('t3', str(op1.value))
                        gen.add_la('t1', '0(t3)')
                    else:
                        gen.add_la('t1', str(contenido.value))
                    
                    if result.isTemp:
                        if 't' in str(result.value):
                            gen.add_move('t3', str(result.value))
                        else:
                            gen.add_li('t3', str(result.value)) 
                        #gen.add_li('t3', str(op2.value))
                        gen.add_lw('t2', '0(t3)')
                    else:
                        gen.add_lw('t2', str(result.value))

                    gen.add_sw('t2', '0(t1)')
                        

            elif self.operacion == TypeAritmetica.SUMA or self.operacion == TypeAritmetica.RESTA:
                
                if contenido.type == Type.INTEGER and result.type == Type.INTEGER:
                    if contenido.isTemp:

                        if 't' in str(contenido.value):
                            gen.add_move('t3', str(contenido.value))
                        else:
                            gen.add_li('t3', str(contenido.value))
                        #gen.add_li('t3', str(op1.value))
                        gen.add_lw('t1', '0(t3)')
                    else:
                        gen.add_lw('t1', str(contenido.value))
                    
                    if result.isTemp:
                        if 't' in str(result.value):
                            gen.add_move('t3', str(result.value))
                        else:
                            gen.add_li('t3', str(result.value)) 
                        #gen.add_li('t3', str(op2.value))
                        gen.add_lw('t2', '0(t3)')
                    else:
                        gen.add_lw('t2', str(result.value))

                elif contenido.type == Type.FLOAT and result.type == Type.FLOAT:
                        gen.add_flw('f0', str(contenido.value))
                        gen.add_flw('f1', str(result.value))

                    
                elif contenido.type == Type.FLOAT and result.type == Type.INTEGER:
                    if result.isTemp:
                        if 't' in str(result.value):
                            gen.add_move('t3', str(result.value))
                        else:
                            gen.add_li('t3', str(result.value))
                        #gen.add_li('t3', str(op1.value))
                        gen.add_lw('t1', '0(t3)')
                    else:
                        gen.add_lw('t1', result.value)

                    gen.comment('Conversion de entero a flotante')
                    gen.add_fcvtsw('f1', 't1')
                    gen.add_flw('f0', str(contenido.value))

                if self.operacion == TypeAritmetica.SUMA:
                    if contenido.type  == Type.INTEGER:
                        gen.add_operation('add', 't0', 't1', 't2')
                        gen.add_la('t3', str(contenido.value))
                        gen.add_sw('t0', '0(t3)')
                    elif contenido.type  == Type.FLOAT:
                        gen.add_operation('fadd.s', 'f2', 'f0', 'f1')
                        gen.add_fsw('f2', str(contenido.value))
                
                elif self.operacion == TypeAritmetica.RESTA:
                    if contenido.type  == Type.INTEGER:
                        gen.add_operation('sub', 't0', 't1', 't2')
                        gen.add_la('t3', str(contenido.value))
                        gen.add_sw('t0', '0(t3)')
                    elif contenido.type  == Type.FLOAT:
                        gen.add_operation('fsub.s', 'f2', 'f0', 'f1')
                        gen.add_fsw('f2', str(contenido.value))
            



            #         result = Aritmetica(self.line, self.col, symL, symR, TypeAritmetica.SUMA).ejecutar(ast, env)
            # elif :
            #         result = Aritmetica(self.line, self.col, symL, symR, TypeAritmetica.RESTA).ejecutar(ast, env)
        
        
            # Existid["var"] = result
            # env.setVariable(self.line, self.col, ast, self.id, Existid)
            # return
           

        list = [f"La constante {self.id} no se le puede cambiar su valor.", self.id, self.line, self.col, "Semantico"]
        ast.setErrors(list)
        return None

