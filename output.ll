; ModuleID = "C:\Users\lucas\OneDrive\Documentos\Projetos\compilador-python-linguagem-stream\compiler\codegen.py"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define void @"main"()
{
entry:
  %".2" = mul i32 10, 10
  %".3" = add i32 %".2", 4
  %".4" = bitcast [5 x i8]* @"fstr" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  ret void
}

@"fstr" = constant [5 x i8] c"%i \0a\00"