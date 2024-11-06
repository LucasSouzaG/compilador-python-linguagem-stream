# coding: utf8
import sys
import os
from lexer import Lexer
from utils import input_folder


if len(input_folder) != 0:
    for arquivos in input_folder:
        if arquivos.endswith('.stream'):
            lex = Lexer(arquivos)
            lex.write_head_file()
            lex.create_stream_py()

            os.system(f"py {lex.file_name}.py")
        else:
            print('Nenhum arquivo .stream localizado no diretório')
else:
    print('Não encontrado arquivos .stream no diretório.')
