import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("qual o nível de dificuldade desejado?")
print("(1) fácil (2) médio (3) difícil")
nivel = int(input("defina o nivel:"))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas  = 15
else:
    total_de_tentativas = 10

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # a função .format() exibe os parametros dentro de suas respectivas chaves
    palpite_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , palpite_str)
    palpite = int(palpite_str)

    if(palpite < 1 or palpite > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue  # aqui o comando continue faz com que toda vez que digitemos um valor errado o loop passe para a próxima tentativa

    acertou = palpite == numero_secreto
    maior   = palpite > numero_secreto
    menor   = palpite < numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break # com o comando BREAK se a condição for verdadeira o loop para
    else: #laço usado em caso de erro
        if(maior):
            print("Você errou! O seu palpite foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu palpite foi menor do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - palpite)
        pontos = pontos - pontos_perdidos

print("Fim do jogo")
