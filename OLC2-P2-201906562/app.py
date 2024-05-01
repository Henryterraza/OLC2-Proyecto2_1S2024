from flask import Flask, request, jsonify
from flask_cors import CORS
from parser.prueba import Parser
from environment.ast import Ast
from environment.generator import Generator
from environment.environment import Environment
from environment.execute import RootExecuter
from environment.types import listaErrores

# Se crea una instancia de la aplicación Flask
app = Flask(__name__)
CORS(app)

# Se define una ruta de Test
@app.route('/ping')
def saludo():
    return f'<h1>pong!</h1>'

@app.route('/interpreter', methods=['POST'])
def recibir_datos():
    # Obtención del código
    jsonObj = request.json
    input_data = jsonObj.get("code")
    # Creación del entorno global
    env = Environment(None, 'GLOBAL')
    # Creación del AST
    ast = Ast()
    gen = Generator(0,0,0,0)
    # Creación del parser
    parser = Parser()
    # [inst1, inst2, inst2]
    print(input_data)
    instructionsArr = parser.interpretar(input_data)

    # print(type(instructionsArr[0]))
    # print(instructionsArr[0].ejecutar(ast, env).value)
    # print(instructionsArr[0].ejecutar(ast, env))
    # print(instructionsArr[0].ejecutar(ast, env).type)

    # Ejecución
    # se agregan los errores lexicos
    for error in listaErrores:
        ast.setErrors(error)
        
    listaErrores.clear()

    RootExecuter(instructionsArr, ast, env, gen, None, None, None)
    print(ast.getConsole())
    print(listaErrores)
    print(env.interfaces)
    # print(env.functions)
    print(env.tabla)
    # Estructurando respuesta
    # res = {"result": True,"console":ast.getConsole(),"errors":ast.getErrors()}
    res = {"consola": gen.get_final_code(), "TablaSimb": ast.getsimbols(), "errores": ast.getErrors()}
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)