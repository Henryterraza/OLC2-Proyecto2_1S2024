
class Ast():
    def __init__(self):
        self.simbols = []
        self.console = ""
        self.errors = []

    def setConsole(self, content):
        self.console += content + "\n"
    
    def getConsole(self):
        return self.console

    def setsimbols(self, simbols):
        self.simbols.append(simbols) 
    
    def getsimbols(self):
        contenido =""
        for simbol in self.simbols:
            contenido += f'''<tr>
      <td>{simbol[0]}</td>
      <td>{simbol[1]}</td>
      <td>{simbol[2]}</td>
      <td>{simbol[3]}</td>
      <td>{simbol[4]}</td>
      <td>{simbol[5]}</td>
    </tr>
    '''
        return contenido
    
    def setErrors(self, errors):
        self.errors.append(errors)
    
    def getErrors(self):
        contenido =""
        for i, Error in enumerate(self.errors):
            contenido += f'''<tr>
      <td>{i+1}</td>
      <td>{Error[0]}</td>
      <td>{Error[1]}</td>
      <td>{Error[2]}</td>
      <td>{Error[3]}</td>
      <td>{Error[4]}</td>
    </tr>
    '''
        return contenido