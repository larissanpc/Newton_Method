import math
def ex1(p0):
  func = p0**3 + 4*p0**2 - 10
  f_linha = 3*p0**2 + 8*p0
  return func, f_linha
  
def ex2(p0):
  func = math.cos(p0) - p0
  f_linha = -math.sin(p0) - 1
  return func, f_linha

def exA(p0):
  func = p0**3 + 4*p0**2 - 10
  f_linha = 2*p0**2 + 8*p0
  return func, f_linha

def exB(p0):
  func = math.cos(p0) - p0
  f_linha = -math.sin(p0) - 1
  return func, f_linha

def exC(p0):
  func = p0**3 - 2*p0**2 - 5
  f_linha = 3*p0**2 - 4*p0
  return func, f_linha

def exD(p0):
  func = math.exp(p0) - 3*p0**2
  f_linha = math.exp(p0) - 6*p0
  return func, f_linha



def newton(f,p0,epsilon):
  #passo 1
  i = 1
  #passo 2
  while i<=10:
    #passo 3
    func, f_linha = f(p0)
    p = p0 - func/f_linha 

    #passo 4 (erro)
    erro = p - p0
    if erro<0:
      erro = erro*-1
    if erro<epsilon:
      print('\nIterações:',i)
      return p
    #passo 5
    i+=1
    #passo 6
    p0 = p
  #passo 7
  print ('O método falhou após 10 iterações')
  print('Procedimento não foi bem-atendido')
  return 0


print('Exercício 1 -> p(n) = ',newton(ex1,1,0.1))
print('Exercício 2 -> p(n) = ',newton(ex2,0.5,0.001))
print('\n')
print('Exercício 2.a -> p(n) = ',newton(exA,1,0.0001))
print('Exercício 2.b -> p(n) = ',newton(exB,0.5,0.0001))
print('Exercício 2.c -> p(n) = ',newton(exC,3,0.0001))
print('Exercício 2.d -> p(n) = ',newton(exD,1,0.0001))
