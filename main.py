# coding: utf8
import sys
import os
from dicionario import Dictionary
from lexer import Lexer

# Verificar se um argumento foi passado
if len(sys.argv) < 2:
    print("Uso: python main.py <nome_do_arquivo>")
    sys.exit(1)

# limpar tela
os.system("cls")

# lexer
dicionario = Dictionary()
print(dicionario.dictionary)

lex = Lexer(sys.argv[1])
lex.write_head_file()
lex.create_stream_py()

# Executar o arquivo gerado
os.system(f"py {lex.file_name}.py")


# with open(sys.argv[1], 'r') as fonte:
#     for linha in fonte:
#         for x in linha.split():
#             for x_, y in dicionario:
#                 match = re.search(re.compile(x_), x)
#                 if match and (x_ == x):
#                     print(f'[ERROR]: line {linha}')
#                     break
#         for (velho, novo) in dicionario:
#             linha = linha.replace(velho, novo)
#         with open(f"{sys.argv[1]}.py", 'a') as f:  # Abrir em modo de anexação
#             f.write(linha)
