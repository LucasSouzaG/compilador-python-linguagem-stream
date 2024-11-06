import sys

from dicionario import Dictionary
from utils import path_input_folder

class Lexer:
    file_name = ""
    dicionario = Dictionary()
    
    def __init__(self, file_name):
        self.file_name = str(file_name)

    def write_head_file(self):
        cabecalho = "#coding: utf8\nimport math\ndef ler(texto):\n  t = raw_input(texto)\n  if t.isdigit():\n    return " \
            "float(t)\n  else:\n    return t\ndef lista(inicio, fim, passo=1):\n  return range(inicio, fim+1, " \
            "passo)\ndef raiz(n, r):\n  return n ** (1/float(r))\ndef texto(n):\n  return str(n)\n"

        with open(f"{self.file_name}.py", 'w') as f:
            f.write(cabecalho)
            
    def create_stream_py(self):
        with open(f"{path_input_folder}\\" + self.file_name, 'r') as fonte:
            for linha in fonte:
                for (velho, novo) in self.dicionario.dictionary:
                    try:
                        linha = linha.replace(velho, novo)
                    except Exception as error:
                        print('velho')
                        print(error)
                with open(f"{self.file_name}.py", 'a') as f:  # Abrir em modo de anexação
                    f.write(linha)
