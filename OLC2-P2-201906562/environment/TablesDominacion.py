from environment.types import Type



# +/-       |Int    |float  |String |char     |Boolean |Array   |Array  |Array     
# Int       |int    |Double |null   |null     |Null    |Null    |Null   |Null     
# float     |Double |Double |null   |null     |Null    |Null    |Null   |Null     
# string    |null   |null   |String |null     |Null    |Null    |Null   |Null     
# char      |null   |null   |null   |null     |Null    |Null    |Null   |Null         
# Boolean   |Null   |Null   |Null   |Null     |Null    |Null    |Null   |Null             
# Array     |Null   |Null   |Null   |Null     |Null    |Null    |Null   |Null         
# struct    |Null   |Null   |Null   |Null     |Null    |Null    |Null   |Null         
# Null      |Null   |Null   |Null   |Null     |Null    |Null    |Null   |Null         




dominant_tableSum = [
    [Type.INTEGER, Type.FLOAT, Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],   
    [Type.FLOAT,   Type.FLOAT, Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.STRING, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
]

dominant_tableRestDivMult = [
    [Type.INTEGER, Type.FLOAT, Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],   
    [Type.FLOAT,   Type.FLOAT, Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
]

dominant_tableModulo = [
    [Type.INTEGER, Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],   
    [Type.NULL,    Type.NULL,   Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL,    Type.NULL,  Type.NULL,   Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
]