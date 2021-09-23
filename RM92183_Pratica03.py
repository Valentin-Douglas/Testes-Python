# Programa de escolha de prêmios da equipe de Dev-Ops Monty Python

# Tela de apresentação do sorteio
print('Seja bem vindo ao sorteio da equipe de Dev-Ops Monty Python')
print('Escolha o console que deseja presentear a equipe na votação: ')
print('Para votar em Playstation: 1')
print('Para votar em Xbox: 2')
print('Para votar em Nintendo: 3')

# Critérios do sorteio

P = int(0)
X = int(0)
N = int(0)
voto = int(0)

# Votação por pessoa
n1 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    P = P+1
elif voto == 2:
    X = X+1
elif voto == 3:
    N = N+1
n2 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    P = P+1
elif voto == 2:
    X = X+1
elif voto == 3:
    N = N+1
n3 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    P = P+1
elif voto == 2:
    X = X+1
elif voto == 3:
    N = N+1
n4 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    P = P+1
elif voto == 2:
    X = X+1
elif voto == 3:
    N = N+1
n5 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    P = P+1
elif voto == 2:
    X = X+1
elif voto == 3:
    N = N+1


# Exibição do resultado da votação
if P >= 3:
    print(f'O prêmio escolhido é o Playstation, com {P} votos!')
elif X >= 3:
    print(f'O prêmio escolhido é o Playstation, com {X} votos!')
elif N >= 3:
    print(f'O prêmio escolhido é o Playstation, com {N} votos!')
else:
    print(f'Tivemos um empate, vamos tentar desempatar semana que vêm!')