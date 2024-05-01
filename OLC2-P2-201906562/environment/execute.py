from environment.types import Type

def RootExecuter(instructionList, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
    print(instructionList)
    for inst in instructionList:
        inst.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)

def StatementExecuter(instructionList, ast, env, gen, lvlbreak, lvlcont, lvlreturno):
    for inst in instructionList:
        res = inst.ejecutar(ast, env, gen, lvlbreak, lvlcont, lvlreturno)
        # if res != None:
        #     if res.type == Type.RETURN:
        #         return res.value
        #     return res
    return None