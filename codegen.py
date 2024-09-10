from llvmlite import ir, binding

class CodeGen():
    def __init__(self):
        self.binding = binding
        self.binding.initialize()
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()

        # Crie o módulo primeiro
        self.module = ir.Module(name=__file__)

        # Declare a função printf
        self._declare_print_function()

        # Configure o LLVM e crie o engine de execução
        self._config_llvm()
        self._create_execution_engine()

    def _config_llvm(self):
        # Configura o LLVM
        self.module.triple = self.binding.get_default_triple()
        func_type = ir.FunctionType(ir.VoidType(), [], False)
        base_func = ir.Function(self.module, func_type, name="main")
        block = base_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        # Verifique se a variável global já foi criada
        if "fstr" not in [gv.name for gv in self.module.global_values]:
            # Criar a string de formato para printf
            str_fmt = "%i \n\0"
            str_type = ir.ArrayType(ir.IntType(8), len(str_fmt))  # Criar array de i8 (bytes)
            format_str = ir.GlobalVariable(self.module, str_type, name="fstr")
            format_str.global_constant = True
            format_str.initializer = ir.Constant(str_type, bytearray(str_fmt.encode("utf8")))


    def _create_execution_engine(self):
        """
        Cria um ExecutionEngine adequado para geração de código JIT na
        CPU do host. O engine é reutilizável para um número arbitrário de
        módulos.
        """
        target = self.binding.Target.from_default_triple()
        target_machine = target.create_target_machine()
        # E um engine de execução com um módulo de suporte vazio
        backing_mod = binding.parse_assembly("")
        engine = binding.create_mcjit_compiler(backing_mod, target_machine)
        self.engine = engine

    def _declare_print_function(self):
        # Declara a função printf
        voidptr_ty = ir.IntType(8).as_pointer()  # Ponteiro para i8 para a string
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        if "printf" not in [f.name for f in self.module.functions]:
            printf = ir.Function(self.module, printf_ty, name="printf")
            self.printf = printf  # Agora printf é um atributo da classe

    def _compile_ir(self):
        """
        Compila a string LLVM IR com o engine fornecido.
        O objeto do módulo compilado é retornado.
        """
        # Cria um objeto do módulo LLVM a partir do IR
        self.builder.ret_void()
        llvm_ir = str(self.module)
        mod = self.binding.parse_assembly(llvm_ir)
        mod.verify()
        # Agora adicione o módulo e certifique-se de que está pronto para execução
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()
        return mod

    def create_ir(self):
        self._compile_ir()

    def save_ir(self, filename):
        with open(filename, 'w') as output_file:
            output_file.write(str(self.module))

