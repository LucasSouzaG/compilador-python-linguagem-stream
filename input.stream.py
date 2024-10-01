#coding: utf8
import math
def ler(texto):
  t = raw_input(texto)
  if t.isdigit():
    return float(t)
  else:
    return t
def lista(inicio, fim, passo=1):
  return range(inicio, fim+1, passo)
def raiz(n, r):
  return n ** (1/float(r))
def texto(n):
  return str(n)
def testando(x):
    return f"eh {x}"

print(3 + 4)
print(testando(10))

for i in range(30):
	if (i%3) == 0 :
		print(f"{i} - Divisivel por 3")
	else:
		print(f"{i} - Nao") 
    #testando(x)

print(3 + 4)
print(testando(10))

for i in range(30):
	if i%3==0 :
		print(f"{i} - Divisivel por 3")
	else:
		print(f"{i} - Nao")