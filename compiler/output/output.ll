; ModuleID = "C:\Users\lucas\OneDrive\Documentos\Projetos\compilador-python-linguagem-stream\compiler\codegen.py"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define void @"main"()
{
code:
  %".2" = sdiv i32 20, 2
  %".3" = bitcast [5 x i8]* @"fstr" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret void
}

@"fstr" = constant [5 x i8] c"%i \0a\00"