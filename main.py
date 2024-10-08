# coding: utf8
import sys
import os

# Verificar se um argumento foi passado
if len(sys.argv) < 2:
    print("Uso: python main.py <nome_do_arquivo>")
    sys.exit(1)

# limpar tela
os.system("cls")

dicionario = [("Corra", "for"),
              ("na", "in"),
              (" faca", ":"),
              ("AteoUltimoHomem", "while"),
              ("TopaOuNaoTopa ", "elif "),
              ("eAssimQueAcaba", "else:"),
              ("entao", ":"),
              ("batmanBegins ", "if "),
              ("BobOConstrutor", "def"),
              (" e ", " and "),
              (" ou ", " or "),
              ("NaoDurma(", "not("),
              ("SemMedoDaVerdade", "True"),
              ("FalsaIdentidade", "False"),
              ("theOffice", "print"),
              ("oRetornoDoJedi", "return"),
              ("Valente", "range")]

cabecalho = "#coding: utf8\nimport math\ndef ler(texto):\n  t = raw_input(texto)\n  if t.isdigit():\n    return " \
            "float(t)\n  else:\n    return t\ndef lista(inicio, fim, passo=1):\n  return range(inicio, fim+1, " \
            "passo)\ndef raiz(n, r):\n  return n ** (1/float(r))\ndef texto(n):\n  return str(n)\n"

with open(f"{sys.argv[1]}.py", 'w') as f:
    f.write(cabecalho)

with open(sys.argv[1], 'r') as fonte:
    for linha in fonte:
        for (velho, novo) in dicionario:
            linha = linha.replace(velho, novo)
        with open(f"{sys.argv[1]}.py", 'a') as f:  # Abrir em modo de anexação
            f.write(linha)

# Executar o arquivo gerado
os.system(f"python {sys.argv[1]}.py")



"with open(sys.argv[1], 'r') as fonte:
    for linha in fonte:
        for x in linha.split():
            for x_, y in dicionario:
                match = re.search(re.compile(x_), x)
                if match and (x_ == x):
                    print(f'[ERROR]: line {linha}')
                    break
        for (velho, novo) in dicionario:
            linha = linha.replace(velho, novo)
        with open(f"{sys.argv[1]}.py", 'a') as f:  # Abrir em modo de anexação
            f.write(linha)"
