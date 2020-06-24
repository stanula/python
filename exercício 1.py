#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
print("exercicio 1")

nota = input("insira uma nota:")
nota_int = int(nota)
maximo = 10

while (nota_int > maximo):
  nova_nota = input("insira uma nota válida:")
  nova_nota_int = int(nova_nota)
  nota_int = nova_nota_int
else:
    print ("nota validada")