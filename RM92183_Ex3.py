# Tela de apresentação da votação
print('Seja bem vindo a votação da Turma de ADS EAD da FIAP')
print('Escolha o dia em que deseja que as lives sejam realizadas: ')
print('Para votar em Segunda-feira: 1')
print('Para votar em Terça-feira: 2')
print('Para votar em Quarta-feira: 3')
print('Para votar em Quinta-feira: 4')
print('Para votar em Sexta-feira: 5')

# Critérios da votação

Segunda = int(0)
Terca = int(0)
Quarta = int(0)
Quinta = int(0)
Sexta = int(0)
voto = int(0)

# Votação por pessoa
v1 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1
v2 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1
v3 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1
v4 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1
v5 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1
v6 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1
v7 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1
v8 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1
v9 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1
v10 = int(input('Informe o RM do participante: '))
voto = int(input('Qual é o seu voto? '))
if voto == 1:
    Segunda = Segunda+1
elif voto == 2:
    Terca = Terca+1
elif voto == 3:
    Quarta = Quarta+1
elif voto == 4:
    Quinta = Quinta+1
elif voto == 5:
    Sexta = Sexta+1

# Exibição do resultado da votação
if Segunda > Terca and Segunda > Quarta and Segunda > Quinta and Segunda > Sexta:
    print(f'As lives serão realizadas as Segundas, dia escolhido com {Segunda} votos!')
elif Terca > Segunda and Terca > Quarta and Terca > Quinta and Terca > Sexta:
    print(f'As lives serão realizadas as Terças, dia escolhido com {Terca} votos!')
elif Quarta > Segunda and Quarta > Terca and Quarta > Quinta and Quarta > Sexta:
    print(f'As lives serão realizadas as Quartas, dia escolhido com {Quarta} votos!')
elif Quinta > Segunda and Quinta > Terca and Quinta > Quarta and Terca > Sexta:
    print(f'As lives serão realizadas as Terças, dia escolhido com {Quinta} votos!')
elif Sexta > Segunda and Sexta > Terca and Sexta > Quarta and Sexta > Quinta:
    print(f'As lives serão realizadas as Terças, dia escolhido com {Sexta} votos!')