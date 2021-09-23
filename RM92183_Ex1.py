# Essa é a atividade onde descobrimos o IMC dos usuários do Gym Quest

print('Olá! Sou o Gym Quest!')

# Primeiro as formalidades rs

nome = str(input('Qual seu nome? '))

print(f'Muito prazer {nome}!')

# Agora vamos conhecer nosso usuário

print('Agora me conte um pouco mais de você!')

altura = float(input('Qual a sua altura? '))

peso = float(input('Qual o seu peso? '))

IMC = peso / (altura ** 2)

if IMC < 16.00:
    print('Você está na categoria Baixo peso - Grau III.')
    print(f'Seu IMC é {IMC:.2}')
elif IMC >= 16.00 and IMC < 16.99:
    print('Você está na categoria Baixo peso - Grau II.')
    print(f'Seu IMC é {IMC:.2}')
elif IMC >= 17.00 and IMC < 18.49:
    print('Você está na categoria Baixo peso - Grau I.')
    print(f'Seu IMC é {IMC:.2}')
elif IMC >= 18.50 and IMC < 24.99:
    print('Você está na categoria Peso Ideal.')
    print(f'Seu IMC é {IMC:.2}')
elif IMC >= 25.00 and IMC < 29.99:
    print('Você está na categoria Sobrepeso.')
    print(f'Seu IMC é {IMC:.2}')
elif IMC >= 30.00 and IMC < 34.99:
    print('Você está na categoria Obesidade Grau I.')
    print(f'Seu IMC é {IMC:.2}')
elif IMC >= 35.00 and IMC < 39.99:
    print('Você está na categoria Obesidade Grau II.')
    print(f'Seu IMC é {IMC:.2}')
else:
    IMC > 40.00
    print('Você está na categoria Obesidade Grau III.')
    print(f'Seu IMC é {IMC:.2}')