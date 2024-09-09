from llvmlite import binding as llvm
from ctypes import CFUNCTYPE, c_int, c_char_p

# Initialize LLVM
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Define the LLVM IR code

llvm_ir = r'''
; ModuleID = "C:\Users\lucas\OneDrive\Documentos\Projetos\compilador-python-linguagem-stream\codegen.py"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define void @"main"()
{
entry:
  %"sum" = add i32 4, 4
  %"sub" = sub i32 %"sum", 2
  %".2" = bitcast [5 x i8]* @"fstr" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"sub")
  %".4" = add i32 4, 4
  %".5" = sub i32 %".4", 2
  %".6" = bitcast [5 x i8]* @"fstr" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  ret void
}

@"fstr" = constant [5 x i8] c"%i \0a\00"
'''





# Create a new LLVM module
module = llvm.parse_assembly(llvm_ir)
target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()
engine = llvm.create_mcjit_compiler(module, target_machine)

# Define the function signature for printf
printf_type = CFUNCTYPE(c_int, c_char_p, c_int)
printf = printf_type(engine.get_function_address("printf"))

# Define the function signature for main
main_type = CFUNCTYPE(None)
main = main_type(engine.get_function_address("main"))

# Call the main function
main()