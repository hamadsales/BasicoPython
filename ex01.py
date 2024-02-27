#Faça um programa que leia um ângulo e informe seu seno, cosseno e tangente
import math
angulo = float(input("Digite um ângulo: "))
anguloRadiano = math.radians(angulo) #Converte o valor em graus para radianos

senoAngulo = math.sin(anguloRadiano) #Retorna o seno em radianos
cossenoAngulo = math.cos(anguloRadiano) #Retorna o cosseno em radianos
tangenteAngulo = math.tan(anguloRadiano) #Retorna a tangente em radianos

print("O ângulo {:.2f} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}".format(angulo,senoAngulo,cossenoAngulo,tangenteAngulo))