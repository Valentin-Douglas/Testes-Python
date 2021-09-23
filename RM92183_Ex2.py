# Programa de mensalidade "Estúdio Mais-You FIAP"

print('Seja bem vindo ao calculador de bonificação do Estúdio Mais-You FIAP')

# Orientação para descobrir o valor do bônus à pagar de acordo com o plano escolhido
faturamento = float(input('Informe o faturamento anual do seu canal: '))
print('Digite B = Basic, S = Silver, G = Gold, P = Plantinum')
plano = str.upper(input('Plano escolhido: '))

#Planos disponíveis
B = float(0.3)
S = float(0.2)
G = float(0.1)
P = float(0.05)

# Resultado do cálculo
if plano == 'B':
    plano = float(B * faturamento)
    print(f'Seu canal terá R${plano:.30} à pagar de bônus anual.')
elif plano == 'S':
    plano = float(S * faturamento)
    print(f'Seu canal terá R${plano:.30} à pagar de bônus anual.')
elif plano == 'G':
    plano = float(G * faturamento)
    print(f'Seu canal terá R${plano:.30} à pagar de bônus anual.')
elif plano == 'P':
    plano = float(P * faturamento)
    print(f'Seu canal terá R${plano:.30} à pagar de bônus anual.')
