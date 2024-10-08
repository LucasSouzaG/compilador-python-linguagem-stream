from llvmlite import ir

class Number():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        i = ir.Constant(ir.IntType(32), int(self.value))  # Use i32
        return i
    
class String():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        return self.value.replace('"', '')
    

class BinaryOp():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right

class Sum(BinaryOp):
    def eval(self):
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i

class Sub(BinaryOp):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i


class Mul(BinaryOp):
    def eval(self):
        return self.builder.mul(self.left.eval(), self.right.eval())

class Div(BinaryOp):
    def eval(self):
        return self.builder.sdiv(self.left.eval(), self.right.eval())


class Print():
    def __init__(self, builder, module, printf, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value

    def eval(self):
        value = self.value.eval()

        # Utilize the existing global variable 'fstr'
        global_fmt = self.module.get_global("fstr")
        if global_fmt is None:
            # Cria uma nova variável global se não existir
            fmt = "%i \n\0"
            c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
            global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
            global_fmt.global_constant = True
            global_fmt.initializer = c_fmt

        fmt_arg = self.builder.bitcast(global_fmt, ir.IntType(8).as_pointer())

        # Call Print Function
        self.builder.call(self.printf, [fmt_arg, value])


