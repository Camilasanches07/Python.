#-Crie um programa que gere um número aleatório que o usuário terá que advinhar. 
#-Solicite ao usuário que insira um palpite
#-Informe ao usuário se o palpite está alto, baixo ou correto do número gerado
#-Conte o núemero de tentativas que o usuário teve
#-Alternativa que pós acertar o número o usuário possa recomeçar
import random

numero_aleatorio = random.randint(1 ,100)
print("Número sorteado para teste", numero_aleatorio)

tentativas = 0

while True:
    print("Escolha um número de 0 a 100: ")
    palpite = int(input("Meu palpite é o número: "))

    if palpite > numero_aleatorio:
        print("Seu palpite está muito alto, escolha outro valor") 
        tentativas += 1 
        print("Número de tentativas: ", tentativas)
    elif palpite < numero_aleatorio:
        print("Seu palpite está muito baixo, escolha outro valor")
        tentativas +=1
        print("Número de tentativas: ", tentativas)
    else:
        tentativas +=1 
        print("Parabéns, você acertou o número")
        print("na tentativa: ", tentativas)
        break 