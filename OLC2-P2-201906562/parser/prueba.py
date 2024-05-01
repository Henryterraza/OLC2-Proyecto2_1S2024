# Librerias
import parser.ply.yacc as yacc
import parser.ply.lex as Lex


# imports
from environment.types import Type, TypeAritmetica, TypeCond, lista, listaErrores
from expressions.primitive import Primitive
from expressions.aritmetica import Aritmetica
from expressions.OperRelacional import OperRelac
from expressions.OperCond import OperCond
from expressions.OperTernario import OperTern
from expressions.AccesVarConst import AccessVarConst
from expressions.AccesInterface import AccessInterface
from expressions.Continue import Continue
from expressions.Break import Break
from expressions.Return import Return
from expressions.parInt import ParInt
from expressions.parFloat import ParFloat
from expressions.toString import toString
from expressions.toLoweCase import toLoCase
from expressions.toUpperCase import toUpCase
from expressions.typeof import typeof
from expressions.LlamadaFunc import LlamaFunc
from expressions.array import Array
from expressions.array_access import ArrayAccess
from expressions.Objectkeys import ObjectKeys
from expressions.ObjectVal import ObjectVal
from expressions.Array_pop import arraypop
from expressions.Array_Indexof import Indexof
from expressions.Array_len import arrayLength
from expressions.Array_join import ArrayJoin
from instrucion.declaracion import Declaration
from instrucion.declaInterface import DeclarInterface
from instrucion.asignacion import Assignment
from instrucion.AsigArray import asignArray
from instrucion.AsigInter import AsigInterface
from instrucion.consolelog import OutConsole
from instrucion.InstIf import If
from instrucion.InstSwitch import Switch
from instrucion.SwitchCase import SwitchCase
from instrucion.SwitchDefault import SwitchDef
from instrucion.Insrwhile import While
from instrucion.InstFor import For
from instrucion.Interface import Interface, newtipe
from instrucion.Funciones import Funciones
from instrucion.array_declaration import ArrayDeclaration
from instrucion.Array_push import arraypush



class codeParams:
    def __init__(self, line, column):
        self.line = line
        self.column = column


#LEXICO
reserved_words = {
    'var': 'VAR',
    'const': 'CONST',
    'float': 'FLOAT',
    'number': 'NUMBER',
    'string': 'STRING',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'console': 'CONSOLE',
    'log': 'LOG',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'while': 'WHILE',
    'for': 'FOR',
    'interface': 'INTERFACE',
    'keys': 'KEYS',
    'values': 'VALUES',
    'function': 'FUNCTION'
}

# Listado de tokens
tokens = [
    'TRUE',
    'FALSE',
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MOD',
    'DOSPTS',
    'PT',
    'PUNTOCOMA',
    'COMA',
    'CADENA',
    'ENTERO',
    'DECIMAL',
    'CARACTER',
    'IG',
    'INTEROGACION',
    'IGIG',
    'DIF',
    'MAYIG',
    'MENIG',
    'MAY',
    'MEN',
    'AND',
    'OR',
    'NOT',
    'ID',
    'LLAVEIZQ',
    'LLAVEDER',
    'CORIZQ',
    'CORDER',
    'TOLOWERCASE',
    'TOUPPERCASE',
    'TYPEOF',
    'PARSEINT',
    'PARSEFLOAT',
    'TOSTRING',
    'PUSH',
    'POP',
    'OBJECT',
    'LENGTH',
    'JOIN',
    'INDEXOF'
] + list(reserved_words.values())



# REGEX
t_MAYIG         = r'>='
t_MENIG         = r'<='
t_MEN           = r'<'
t_MAY           = r'>'
t_PARIZQ        = r'\('
t_PARDER        = r'\)'
t_LLAVEIZQ      = r'\{'
t_LLAVEDER      = r'\}'
t_CORIZQ        = r'\['
t_CORDER        = r'\]'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIVIDIDO      = r'/'
t_MOD           = r'%'
t_DOSPTS        = r'\:'
t_PT            = r'\.'
t_PUNTOCOMA     = r';'
t_COMA          = r','
t_IGIG          = r'=='
t_DIF           = r'!='
t_IG            = r'='
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_INTEROGACION  = r'\?'

#Función de reconocimiento
def t_LENGTH(t):
    r'length'
    return t

def t_JOIN(t):
    r'join'
    return t

def t_PUSH(t):
    r'push'
    return t

def t_INDEXOF(t):
    r'indexOf'
    return t

def t_POP(t):
    r'pop'
    return t

def t_OBJECT(t):
    r'Object'
    return t

def t_TOUPPERCASE(t):
    r'toUpperCase'
    return t

def t_TOLOWERCASE(t):
    r'toLowerCase'
    return t

def t_TOSTRING(t):
    r'toString'
    return t

def t_PARSEFLOAT(t):
    r'parseFloat'
    return t

def t_PARSEINT(t):
    r'parseInt'
    return t

def t_TYPEOF(t):
    r'typeof'
    return t



def t_CARACTER(t):
    r'\'.?\''
    try:
        chrValue = str(t.value[1:-1])
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, str(chrValue), Type.CHAR)
    except ValueError:
        print("Error al convertir string %d", t.value)
        t.value = Primitive(0, 0, None, Type.NULL)
    return t



def t_CADENA(t):
    r'\"([^"\\]|(\\.)?)*\"'
    try:
        strValue = str(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, strValue[1:-1], Type.STRING)
    except ValueError:
        print("Error al convertir string %d", t.value)
        t.value = Primitive(0, 0, None, Type.NULL)
    return t


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        floatValue = float(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, floatValue, Type.FLOAT)
    except ValueError:
        print("Error al convertir a decimal %d", t.value)
        t.value = Primitive(0, 0, None, Type.NULL)
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        intValue = int(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, intValue, Type.INTEGER)
    except ValueError:
        print("Error al convertir a entero %d", t.value)
        t.value = Primitive(0, 0, None, Type.NULL)
    return t

def t_TRUE(t):
    r'true'
    try:
        Value = True
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, Value, Type.BOOLEAN)
    except ValueError:
        print("Error al convertir a entero %d", t.value)
        t.value = Primitive(0, 0, None, Type.NULL)
    return t

def t_FALSE(t):
    r'false'
    try:
        Value = False
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, Value, Type.BOOLEAN)
    except ValueError:
        print("Error al convertir a entero %d", t.value)
        t.value = Primitive(0, 0, None, Type.NULL)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value.lower(),'ID')
    return t



t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    tok_line_start = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
    line_num = t.lexer.lexdata.count('\n', 0, t.lexpos) + 1
    col_num = t.lexpos - tok_line_start
    listTemp = [f"Caracter {t.value[0]} no reconocido " , "", line_num, col_num, "Lexico"]
    listaErrores.append(listTemp)
    t.lexer.skip(1)

#SINTACTICO
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','IGIG','DIF'),
    ('left','MAY','MAYIG', 'MEN', 'MENIG'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO', 'MOD'),
    ('right', 'NOT', 'UMENOS'),
)

#START
def p_instrucciones_lista(t):
    '''instrucciones : instrucciones instruccion 
                    | instruccion '''
   
    arr = []
    if 2 < len(t):
        t[1].append(t[2])
        arr = t[1]
    else:
        arr.append(t[1])
        
    t[0] = arr
   
#Listado de instrucciones
def p_instruccion(t):
    '''instruccion : declaracionvar PUNTOCOMA
                    | declaracionconst PUNTOCOMA
                    | arraydeclarationVar PUNTOCOMA
                    | arraydeclarationConst PUNTOCOMA
                    | asignacion PUNTOCOMA
                    | AsigInter PUNTOCOMA
                    | OptenInterface 
                    | OperTernario PUNTOCOMA
                    | SentCtrflujo
                    | SentTransf PUNTOCOMA    
                    | consolelog PUNTOCOMA
                    | FuncDeb PUNTOCOMA
                    | FuncEspe PUNTOCOMA
                    | FunInterface PUNTOCOMA  
                    | FuncArray PUNTOCOMA  
                    | Funciones    
                    | LLamaFunciones PUNTOCOMA'''    
    t[0] = t[1]


# gramatica para ver si una llamada de funcion con o sin parametros
def p_FuncArrayJoin(t):
    '''FuncArray  : ID PT JOIN PARIZQ PARDER'''
    params = get_params(t)
    t[0] = ArrayJoin(params.line, params.column, t[1])

def p_FuncArrayLen(t):
    '''FuncArray  : ID PT LENGTH'''
    params = get_params(t)
    t[0] = arrayLength(params.line, params.column, t[1])

def p_FuncArrayIndex(t):
    '''FuncArray  : ID PT INDEXOF PARIZQ expresion PARDER'''
    params = get_params(t)
    t[0] = Indexof(params.line, params.column, t[1], t[5])

def p_FuncArrayPop(t):
    '''FuncArray  : ID PT POP PARIZQ PARDER'''
    params = get_params(t)
    t[0] = arraypop(params.line, params.column, t[1])

def p_FuncArray(t):
    '''FuncArray  : ID PT PUSH PARIZQ expresion PARDER'''
    params = get_params(t)
    t[0] = arraypush(params.line, params.column, t[1], t[5])


# gramatica para ver si una llamada de funcion con o sin parametros
def p_LLamaFuncionesCP(t):
    '''LLamaFunciones  : ID PARIZQ PARDER'''
    params = get_params(t)
    t[0] = LlamaFunc(params.line, params.column, t[1], [])


def p_LLamaFuncionesSP(t):
    '''LLamaFunciones  : ID PARIZQ ListExpresion PARDER'''
    params = get_params(t)
    t[0] = LlamaFunc(params.line, params.column, t[1], t[3])


# aqui se verifica si es de un tipo de funcion con o sin parametros, con o sin retorno
def p_FuncionesSPCR(t):
    '''Funciones  : FUNCTION ID PARIZQ PARDER DOSPTS type LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
    t[0] = Funciones(params.line, params.column, t[2], [], t[6], t[8])

def p_FuncionesSPSR(t):
    '''Funciones  : FUNCTION ID PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
    t[0] = Funciones(params.line, params.column, t[2], [], None, t[6])

def p_FuncionesCPSR(t):
    '''Funciones  : FUNCTION ID PARIZQ LisParat PARDER  LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
    t[0] = Funciones(params.line, params.column, t[2], t[4], None, t[7])

def p_FuncionesCPCR(t):
    '''Funciones  : FUNCTION ID PARIZQ LisParat PARDER DOSPTS type LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
    t[0] = Funciones(params.line, params.column, t[2], t[4], t[7], t[9])


def p_LisParat(t):
    '''LisParat : LisParat COMA parametro
                    | parametro'''
    
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

def p_parametro(t):
    '''parametro : ID DOSPTS type'''
    t[0] = [t[1], t[3]]



def p_OptenInterface(t):
    '''OptenInterface  : ID PT ID'''
    params = get_params(t)
    t[0] = AccessInterface(params.line, params.column, t[1], t[3])



def p_FunInterface(t):
    '''FunInterface : INTERFACE ID LLAVEIZQ Listatributos LLAVEDER'''        
    params = get_params(t)
    t[0] = Interface(params.line, params.column, t[2], t[4])

def p_Listatributos(t):
    '''Listatributos : Listatributos PUNTOCOMA atributo
                    | atributo'''
    
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

def p_atributo(t):
    '''atributo : ID DOSPTS type'''
    t[0] = [t[1], t[3]]


#apartado de funciones especiales
def p_FuncEspKeys(t):
    '''FuncEspe : OBJECT PT KEYS PARIZQ expresion PARDER'''        
    params = get_params(t)
    t[0] = ObjectKeys(params.line, params.column, t[5])

def p_FuncEspeVal(t):
    '''FuncEspe : OBJECT PT VALUES PARIZQ expresion PARDER'''        
    params = get_params(t)
    t[0] = ObjectVal(params.line, params.column, t[5])


#apartado de parseos
def p_FuncDebInt(t):
    '''FuncDeb : PARSEINT PARIZQ expresion PARDER'''        
    params = get_params(t)
    t[0] = ParInt(params.line, params.column, t[3])

def p_FuncDebFloat(t):
    '''FuncDeb : PARSEFLOAT PARIZQ expresion PARDER'''        
    params = get_params(t)
    t[0] = ParFloat(params.line, params.column, t[3])

def p_FuncDebString(t):
    '''FuncDeb : FALSE PT TOSTRING PARIZQ  PARDER        
                | TRUE PT TOSTRING PARIZQ  PARDER        
                | ID PT TOSTRING PARIZQ  PARDER'''
    params = get_params(t)
    t[0] = toString(params.line, params.column, t[1])

def p_FuncDeblower(t):
    '''FuncDeb : ID PT TOLOWERCASE PARIZQ  PARDER'''        
    params = get_params(t)
    t[0] = toLoCase(params.line, params.column, t[1])

def p_FuncDebUpper(t):
    '''FuncDeb : ID PT TOUPPERCASE PARIZQ  PARDER'''        
    params = get_params(t)
    t[0] = toUpCase(params.line, params.column, t[1])

def p_FuncDebtypeof(t):
    '''FuncDeb : TYPEOF expresion'''        
    params = get_params(t)
    t[0] = typeof(params.line, params.column, t[2])



def p_consolelog(t):
    '''consolelog : CONSOLE PT LOG PARIZQ ListExpresion PARDER'''        
    params = get_params(t)
    t[0] = OutConsole(params.line, params.column, t[5])


def p_Listexp(t):
    '''ListExpresion : ListExpresion COMA expresion        
                    | expresion '''        
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

def p_SentCtrflujo(t):
    '''SentCtrflujo : Sentenciaif
                    | SentenciaSwitch        
                    | SentenciaWhile       
                    | SentenciaFor'''        
    t[0] = t[1]

def p_SentenciaFor(t):
    '''SentenciaFor : FOR PARIZQ VAR ID DOSPTS type IG expresion PUNTOCOMA ID MENIG expresion PUNTOCOMA ID MAS MAS PARDER LLAVEIZQ instrucciones LLAVEDER'''        
    params = get_params(t) 
    dec = Declaration(params.line, params.column, "const", t[4], t[6], t[8])    
    t[0] = For(params.line, params.column, dec, t[6], t[4], t[10], t[14], t[8], t[12], t[19])

def p_SentenciaWhile(t):
    '''SentenciaWhile : WHILE PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER'''        
    print(t[6])
    params = get_params(t)       
    t[0] = While(params.line, params.column, t[3], t[6])

def p_SentenciaSwitch(t):
    '''SentenciaSwitch : SWITCH PARIZQ expresion PARDER LLAVEIZQ listCase LLAVEDER'''        
    print(t[6])
    params = get_params(t)       
    t[0] = Switch(params.line, params.column, t[3], t[6])


def p_listCase(t):
    '''listCase : listCase oplist        
                | oplist'''        
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[2]]
    else:
        arr.append(t[1])
    t[0] = arr

def p_oplist_Case(t):
    '''oplist : CASE expresion DOSPTS instrucciones''' 
    params = get_params(t)       
    t[0] = SwitchCase(params.line, params.column, t[2], t[4])

def p_oplist_Default(t):
    '''oplist : DEFAULT DOSPTS instrucciones''' 
    params = get_params(t)       
    t[0] = SwitchDef(params.line, params.column, t[3])


def p_Sentenciaif(t):
    '''Sentenciaif : IF  PARIZQ expresion PARDER LLAVEIZQ instrucciones  LLAVEDER
                    | IF  PARIZQ expresion PARDER LLAVEIZQ instrucciones  LLAVEDER ELSE LLAVEIZQ instrucciones LLAVEDER 
                    | IF  PARIZQ expresion PARDER LLAVEIZQ instrucciones  LLAVEDER ELSE Sentenciaif'''
    params = get_params(t)
    if 8 == len(t):
        t[0] = If(params.line, params.column, t[3], t[6], None, None)
    elif 12 == len(t):
        t[0] = If(params.line, params.column, t[3], t[6], t[10], None)
    else:
        t[0] = If(params.line, params.column, t[3], t[6], None, t[9])


def p_SentTransfBreak(t):
    '''SentTransf : BREAK''' 
    params = get_params(t)       
    t[0] = Break(params.line, params.column)

def p_SentTransfCont(t):
    '''SentTransf : CONTINUE'''  
    params = get_params(t)      
    t[0] = Continue(params.line, params.column)

def p_SentTransfRet(t):
    '''SentTransf : RETURN'''  
    params = get_params(t)      
    t[0] = Return(params.line, params.column, None)

def p_SentTransfExp(t):
    '''SentTransf : RETURN expresion'''  
    params = get_params(t)      
    t[0] = Return(params.line, params.column, t[2])





def p_OperTernario(t):
    '''OperTernario : expresion INTEROGACION  expresion DOSPTS expresion'''
    params = get_params(t)
    t[0] = OperTern(params.line, params.column, t[3], t[5], t[1])

# Asignacion a interface
def p_AsigInter(t):
    '''AsigInter : ID PT ID IG expresion
                    | ID PT ID MAS IG expresion 
                    | ID PT ID MENOS IG expresion''' 
    params = get_params(t)

    if 6 == len(t):
        t[0] = AsigInterface(params.line, params.column, t[1], t[3], t[5], TypeAritmetica.ASIGNACION)
    elif 7 == len(t):
        if t[4] == "+":
            t[0] = AsigInterface(params.line, params.column, t[1], t[3], t[6], TypeAritmetica.SUMA)
        else:
            t[0] = AsigInterface(params.line, params.column, t[1], t[3], t[6], TypeAritmetica.RESTA)




# asignacion a varibles 
def p_asignacion(t):
    '''asignacion : ID IG expresion
                    | ID MAS IG expresion  
                    | ID MENOS IG expresion''' 
    params = get_params(t)

    if 4 == len(t):
        t[0] = Assignment(params.line, params.column, t[1], t[3], TypeAritmetica.ASIGNACION)
    elif 5 == len(t):
        if t[2] == "+":
            t[0] = Assignment(params.line, params.column, t[1], t[4], TypeAritmetica.SUMA)
        else:
            t[0] = Assignment(params.line, params.column, t[1], t[4], TypeAritmetica.RESTA)


def p_asignacionArray(t):
    '''asignacion : accesId CORIZQ expresion CORDER IG expresion''' 
    params = get_params(t)
    t[0] = asignArray(params.line, params.column, t[1], t[3], t[6])



# Declaracion de variables var const y variables interface
def p_declaracionvar(t):
    '''declaracionvar : VAR ID DOSPTS type IG expresion
                        | VAR ID DOSPTS type
                        | VAR ID IG expresion''' 
    params = get_params(t)
    if 7 == len(t):
        t[0] = Declaration(params.line, params.column, t[1], t[2], t[4], t[6])
    elif 5 == len(t):
        if str(t[3]) == ":":
            t[0] = Declaration(params.line, params.column, t[1], t[2], t[4], None)
        else:
            t[0] = Declaration(params.line, params.column, t[1], t[2], None, t[4])


def p_declaracionvarInterface(t):
    '''declaracionvar : VAR ID DOSPTS ID IG LLAVEIZQ ListAtrib LLAVEDER''' 
    params = get_params(t)
    t[0] = DeclarInterface(params.line, params.column, t[2], t[4], t[7])


def p_ListAtrib(t):
    '''ListAtrib : ListAtrib COMA atrib
                    | atrib'''
    
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

def p_atrib(t):
    '''atrib : ID DOSPTS expresion'''
    t[0] = [t[1], t[3]]



def p_declaracionconst(t):
    '''declaracionconst : CONST ID DOSPTS type IG expresion
                        | CONST ID DOSPTS type
                        | CONST ID IG expresion''' 
    params = get_params(t)
    if 7 == len(t):
        t[0] = Declaration(params.line, params.column, t[1], t[2], t[4], t[6])
    elif 5 == len(t):
        if str(t[3]) == ":":
            t[0] = Declaration(params.line, params.column, t[1], t[2], t[4], None)
        else:
            t[0] = Declaration(params.line, params.column, t[1], t[2], None, t[4])


# Tipo de variables
def p_type_prod(t):
    '''type : NUMBER
            | FLOAT
            | STRING
            | BOOLEAN
            | CHAR'''
    
    if t[1] == 'number':
        t[0] = Type.INTEGER
    if t[1] == 'float': 
        t[0] = Type.FLOAT
    if t[1] == 'string':
        t[0] = Type.STRING
    if t[1] == 'boolean':
        t[0] = Type.BOOLEAN
    if t[1] == 'char':
        t[0] = Type.CHAR

def p_type_Inter(t):
    '''type : ID'''

    if str(t[1]) in lista:
        new = newtipe(str(t[1]), lista.index(str(t[1])))
        t[0] = new
    else:
        new = newtipe(str(t[1]), len(lista))
        lista.append(str(t[1]))
        t[0] = new
        

        



#  apartado de expresiones condicionales
        
def p_expresion_AND(t):
    '''expresion : expresion AND expresion'''
    params = get_params(t)
    t[0] = OperCond(params.line, params.column, t[1], t[3], TypeCond.AND)


def p_expresion_OR(t):
    '''expresion : expresion OR expresion'''
    params = get_params(t)
    t[0] = OperCond(params.line, params.column, t[1], t[3], TypeCond.OR)

def p_expresion_NOT(t):
    '''expresion : NOT expresion'''
    params = get_params(t)
    t[0] = OperCond(params.line, params.column, t[2], None, TypeCond.NOT)



#  apartado de expresion operacion relacional
def p_OperRelacional_May(t):
    '''expresion : expresion MAY expresion '''
    params = get_params(t)
    t[0] = OperRelac(params.line, params.column, t[1], t[3], TypeCond.MAY)

def p_OperRelacional_Men(t):
    '''expresion : expresion MEN expresion '''
    params = get_params(t)
    t[0] = OperRelac(params.line, params.column, t[1], t[3], TypeCond.MEN)

def p_OperRelacional_MayIg(t):
    '''expresion : expresion MAYIG expresion '''
    params = get_params(t)
    t[0] = OperRelac(params.line, params.column, t[1], t[3], TypeCond.MAYEQ)

def p_OperRelacional_MenIg(t):
    '''expresion : expresion MENIG expresion '''
    params = get_params(t)
    t[0] = OperRelac(params.line, params.column, t[1], t[3], TypeCond.MENEQ)

def p_OperRelacional_IgIg(t):
    '''expresion : expresion IGIG expresion '''
    params = get_params(t)
    t[0] = OperRelac(params.line, params.column, t[1], t[3], TypeCond.EQUAL)

def p_OperRelacional_Dif(t):
    '''expresion : expresion DIF  expresion '''
    params = get_params(t)
    t[0] = OperRelac(params.line, params.column, t[1], t[3], TypeCond.DIF)


#  apartado de expresion aritmetica
def p_expresion_mas(t):
    'expresion : expresion MAS expresion'
    params = get_params(t)
    t[0] = Aritmetica(params.line, params.column, t[1], t[3], TypeAritmetica.SUMA)

def p_expresion_menos(t):
    'expresion : expresion MENOS expresion'
    params = get_params(t)
    t[0] = Aritmetica(params.line, params.column, t[1], t[3], TypeAritmetica.RESTA)

def p_expresion_por(t):
    'expresion : expresion POR expresion'
    params = get_params(t)
    t[0] = Aritmetica(params.line, params.column, t[1], t[3], TypeAritmetica.MULT)


def p_expresion_div(t):
    'expresion : expresion DIVIDIDO expresion'
    params = get_params(t)
    t[0] = Aritmetica(params.line, params.column, t[1], t[3], TypeAritmetica.DIV)

def p_expresion_mod(t):
    'expresion : expresion MOD expresion'
    params = get_params(t)
    t[0] = Aritmetica(params.line, params.column, t[1], t[3], TypeAritmetica.MOD)

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    params = get_params(t)
    t[0] = Aritmetica(params.line, params.column, t[2], t[2], TypeAritmetica.UMENOS)


def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | CADENA
                    | DECIMAL
                    | TRUE
                    | FALSE
                    | CARACTER
                    | FuncDeb
                    | FuncEspe
                    | OperTernario
                    | OptenInterface
                    | LLamaFunciones 
                    | FuncArray
                    | listArray'''
    t[0] = t[1]

def p_expresion_id(t):
    '''expresion    : ID'''
    params = get_params(t)
    t[0] = AccessVarConst(params.line, params.column, t[1])

def p_expresion_array_primitiva(t):
    '''expresion : CORIZQ ListExpresion CORDER'''
    params = get_params(t)
    t[0] = Array(params.line, params.column, t[2])


def p_expresion_list_array(t):
    '''listArray : accesId CORIZQ expresion CORDER'''
    params = get_params(t)
    if len(t) > 4:
        t[0] = ArrayAccess(params.line, params.column, t[1], t[3])
        # t[0] = InterfaceAccess(params.line, params.column, t[1], t[3])



def p_accesId(t):
    '''accesId : ID'''
    params = get_params(t)
    t[0] = AccessVarConst(params.line, params.column, t[1])



def p_instruction_array_declarationVar(t):
    'arraydeclarationVar : VAR ID DOSPTS type CORIZQ CORDER IG expresion'
    params = get_params(t)
    t[0] = ArrayDeclaration(params.line, params.column, t[1], t[2], t[4], t[8])

def p_instruction_array_declarationVarConst(t):
    'arraydeclarationConst : CONST ID DOSPTS type CORIZQ CORDER IG expresion'
    params = get_params(t)
    t[0] = ArrayDeclaration(params.line, params.column, t[1], t[2], t[4], t[8])



def p_error(p):
    if p:
        listTemp = [f"Token esperado ; " , "", p.lineno, p.lexpos, "Sintactico"]
        listaErrores.append(listTemp)
    else:
        print("Error de sintaxis")


def get_params(t):
    line = t.lexer.lineno  # Obtener la línea actual desde el lexer
    lexpos = t.lexpos if isinstance(t.lexpos, int) else 0  # Verificar si lexpos es un entero
    column = lexpos - t.lexer.lexdata.rfind('\n', 0, lexpos) 
    return codeParams(line, column)




class Parser:
    def __init__(self):
        pass

    def interpretar(self, input):
        lexer = Lex.lex()
        parser = yacc.yacc()
        result = parser.parse(input)
        return result