from interface.expression import Expression
from environment.value import Value
from environment.types import Type

class Primitive(Expression):
    def __init__(self, line, col, value, type):
        self.line = line
        self.col = col
        self.value = value
        self.type = type

    def ejecutar(self, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
        if(self.type == Type.INTEGER):
            temp = gen.new_temp()
            gen.add_br()
            gen.comment('Agregando un primitivo numerico')
            gen.add_li('t0', str(self.value))
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
            return  Value(str(temp), True, self.type, [], [], [])
        elif (self.type == Type.STRING):
            tempString = gen.new_string()
            gen.comment('Agregando un primitivo numerico')
            nameId = 'str_'+str(tempString)
            nameIdType = 'str_'+str(tempString) +'.typeof'
            gen.variable_data(nameId, 'string', '\"'+str(self.value)+'\"')
            gen.variable_data(nameIdType, 'string', '\"String\"')
            return  Value(nameId, False, self.type, [], [], [])
        elif (self.type == Type.FLOAT):
            tempFloat = gen.new_float()
            gen.comment('Agregando un primitivo numerico')
            nameId = 'Flt_'+str(tempFloat)
            nameIdType = 'Flt_'+str(tempFloat) +'.typeof'
            gen.variable_data(nameId, 'float', str(self.value))
            gen.variable_data(nameIdType, 'string', '\"Float\"')
            return  Value(nameId, False, self.type, [], [], [])
        elif (self.type == Type.BOOLEAN):
            gen.comment('Agregando un primitivo numerico')
            temp = gen.new_temp()
            gen.add_br()
            if self.value:
                gen.add_li('t0', '1')
            else:
                gen.add_li('t0', '0')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
                
            return  Value(str(temp), True, self.type, [], [], [])