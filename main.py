from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.codegen import CodeGen
from compiler.run_code import  run_code

fname = "input.stream"

with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.ll")

with open('compiler\output\output.ll') as f:
    run_code(f.read())