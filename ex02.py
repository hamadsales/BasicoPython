#Sorteando um aluno
import random

aluno1 = input("Digite o nome do 1° Aluno: ")
aluno2 = input("Digite o nome do 2° Aluno: ")
aluno3 = input("Digite o nome do 3° Aluno: ")
aluno4 = input("Digite o nome do 4° Aluno: ")

alunoSorteado = random.randint(1,4)


if alunoSorteado == 1:
    print('O 1° aluno {}, foi sorteado!'.format(aluno1))
elif alunoSorteado == 2:
    print('O 2° aluno {}, foi sorteado!'.format(aluno2))
elif alunoSorteado == 3:
    print('O 3° aluno {}, foi sorteado!'.format(aluno3))
elif alunoSorteado == 4:
    print('O 4° aluno {}, foi sorteado!'.format(aluno4))
else:
    print("Erro!")

#Outra forma de resolver
listaDeAlunos = [aluno1,aluno2,aluno3,aluno4]
alunoEscolhido = random.choice(listaDeAlunos) #Escolhe um elemento aleatório
print('O aluno {}, foi sorteado!'.format(alunoEscolhido))


#sorteando os alunos em sequência aleatória
sorteio1 = random.randint(1,4)
sorteio2 = random.randint(1,4)

while sorteio1 == sorteio2:
    sorteio2 = random.randint(1, 4)
if sorteio1 != sorteio2:
    sorteio3 = random.randint(1,4)
    while sorteio3 == sorteio2:
        sorteio3 = random.randint(1, 4)
    while sorteio3 == sorteio1:
        sorteio3 = random.randint(1, 4)
    if sorteio3 != sorteio2 and sorteio3 != sorteio1:
        sorteio4 = random.randint(1,4)
        while sorteio4 == sorteio1:
            sorteio4 = random.randint(1, 4)
        while sorteio4 == sorteio2:
            sorteio4 = random.randint(1, 4)
        while sorteio4 == sorteio3:
            sorteio4 = random.randint(1, 4)
        print("A sequência é {} {} {} {}".format(sorteio1, sorteio2, sorteio3, sorteio4))

#Outra forma
listaDeAlunos = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(listaDeAlunos)

print(listaDeAlunos)