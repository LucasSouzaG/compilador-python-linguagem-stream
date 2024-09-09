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