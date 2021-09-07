# Esse programa é um stromelet de pombo obeso, logo vamos refazendo e melhorando ao longo do tempo #

print("Olá mundo!")

# Primeiro as formalidades rs

nome = input("Qual seu nome? ")

valor1 = input("Qual a sua idade? ")

valor2 = input("Em que ano estamos? ")

idade = int(valor2) - int(valor1)

print(nome, ", você nasceu em ", idade)

# Agora vamos conhecer nosso usuário

print("Agora me conte um pouco mais de você!")

altura = float(input("Qual a sua altura? "))

peso = float(input("Qual o seu peso? "))

IMC = (altura / peso) ** 2

print(f'Seu IMC é {IMC:.2}')
