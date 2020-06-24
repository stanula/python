#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

print ("exercício 2")

usuario = input("nome de usuário:")
senha = input("senha:")

while (usuario == senha):
    print ("sua senha não pode ser igual seu nome de usuário!")
    novo_usuario = input("nome de usuário:")
    nova_senha = input("senha:")
    senha = nova_senha
    usuario = novo_usuario
else:
    print("senha definida com sucesso")