from enum import Enum

class Type(Enum):
    INTEGER = 0
    FLOAT = 1
    STRING = 2
    CHAR = 3
    BOOLEAN = 4
    ARRAY = 5
    STRUCT = 6
    NULL = 7
    BREAK = 8
    CONTINUE = 9
    RETURN = 10

def get_key(enum_class, value):
   try:
       return enum_class[value]
   except KeyError:
       return None
   
def add_key(enum_class, key, valor):
    setattr(enum_class, key, valor)

class TypeAritmetica(Enum):
  SUMA  = 0
  RESTA = 1
  MULT  = 2
  DIV   = 3
  MOD   = 4
  UMENOS= 5
  ASIGNACION = 6


class TypeCond(Enum):
  EQUAL = 0
  DIF   = 1
  MEN   = 2
  MENEQ = 3
  MAY   = 4
  MAYEQ = 5
  AND   = 6
  OR    = 7
  NOT   = 8  
  
lista = ["number", "float", "string", "char", "boolean", "array", "struct","null","break", "continue","return"]
listaErrores = []


class StringType():
  def Retorno(type):
    return lista[type]
   
  def GetSize():
    return len(lista)
  
  def Setlist(dato):
    lista.append(dato)

class Reser_Words():
   def Verificar(type: str):
    list = ["if", "else", "break", "default", "case", "switch", "console", "log", "while", "for", "continue", "return", "function", "interface" "const", "var", "number", "float", "string", "char", "bool", "array", "struct", "null", "true", "false"]

    for word in list:
      if word == type:
        return True

    return False