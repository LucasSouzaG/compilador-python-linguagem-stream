# coding: utf8
import sys
import os
from dicionario import Dictionary
from lexer import Lexer

cam = os.getcwd() + '\\input'
cam_dir = os.listdir(cam)
if len(cam_dir) != 0:
    for arquivos in cam_dir:
        if arquivos.endswith('.stream'):
            dicionario = Dictionary()

            lex = Lexer(arquivos)
            lex.write_head_file()
            lex.create_stream_py()

            os.system(f"py {lex.file_name}.py")
        else:
            print('Nenhum arquivo .stream localizado no diretório')

else:
    print('Não encontrado arquivos .stream no diretório.')
