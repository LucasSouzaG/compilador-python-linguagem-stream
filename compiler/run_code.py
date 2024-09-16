from llvmlite import binding as llvm
from ctypes import CFUNCTYPE, c_int, c_char_p

# Initialize LLVM
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Define the LLVM IR code

def run_code(code_llvm):
    llvm_ir = fr'''{code_llvm}'''

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