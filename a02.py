#Operadores aritméticos
import math #importa a biblioteca math

n1 = pow(4,3)#Retorna 4 elevado a 3
n2 = 4**3 #Retorna 4 elevado a 3
n3 = 81**(1/2) #Retorna a raiz quadrada de 81
n4 = math.sqrt(81) #retorna a raiz quadrada de 81
n5 = 124**(1/3) #retorna a raiz cúbica de 125

print(n1,n2,n3,n4,n5)
#abaixo vamos formatar o n5 para ter 2 casas decimais
print('A raiz cúbica de 124 é {:.2f}'.format(n5))