# CALCULADORA

##   O intuito deste projeto é desenvolver suas habilidades e conhecimento do que foiabordade até o momento, através do desenvolvimento de uma calculadora básica que  deverá conter as seguintes funcionalidade: 
## 1- Operações matematicas(soma, subtração, multiplicação, divisão).
## 2- Equação do segundo grau
## 3- Calculo de área do quadrado
## 3- Calculo de área do circulo
## 4- Calculo do volume do circulo
## 5-Menu => onde ele exibe as opções para o usuário escolher qual calculo deseja realizar 
## E por fim uma opção para encerrar o programa

# ESTRUTURA
## A estrutura básica da calculadora é a seguinte:
```python
def soma(a,b):
  pass
def sub(a,b):
  pass
def div(a,b):
  pass
def mult(a,b):
  pass
def eq2grau(a,b,c):
  pass
def areaQuadrado(lado):
  pass
def areaCirculo(raio):
  pass
def volumeEsfera(raio):
  pass
def menu():
  op=-1
  passou = True
  while True:
    print('1 - Soma')
    print('2 - Subtração')
    print('0 - Sair')
    # e assim por diante

    # essa parte do código é para evitar quando a pessoa digita alguma coisa
    # diferente de um número
    op = int(input('Escolha uma opção'))
    if op = 1:
      n1 = float(input('Digite o primeiro número'))
      n2 = float(input('Digite o segundo número'))
      print('A soma entre ',n1,' e ',n1,' é: ',soma(n1,n2))
    if op = 2:
      n1 = float(input('Digite o primeiro número'))
      n2 = float(input('Digite o segundo número'))
      print('A subtração entre ',n1,' e ',n1,' é: ',sub(n1,n2))
    elif op == 0:
      print('Encerrando Programa')
      break
    else:
      print('Opção inválida digite outro número')
```
# OBSERVAÇÕE
## As seguintes validações precisam ser realizadas:
### 1 - DIVISÃO POR ZERO NÃO PODE
### 2 - O DELTA NA EQUAÇÃO DE 2° DEVE SER MAIOR OU IGUAL A ZERO
### 3 - NAS FUNÇÕES DE AREA E VOLUME O LADO E O RAIO DEVEM SER POSITIVOS
### 4 - Quando for realizar os calculos que necessitam de pi use o da biblioteca mathque deve aparecer na primeira linha do programa
```python
from math import pi
# A PARTIR DAQUI VEM O SEU PROGRAMA
```


