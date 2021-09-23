# Programa de escolha de viagens e descontos proporcionais

print('Seja bem vindo à nossa loja de pacotes aéreos VOE SEMPRE CONOSCO.com')
print('Escolha a categoria de assento de sua preferência: ')
print(' Econômica: E - 500 por pessoa')
print(' Executiva: EX - 1000 por pessoa')
print(' Primeira Classe: PC 2500 por pessoa')

# Tela de apresentação do site e instruções de como escolher o pacote
categ = str(input('Informe a categoria desejada: '))
E = int(500)
EX = int(1000)
PC = int(2500)
qtd_psg = int(input('Informe a quantidade de assentos desejados: '))

#Exibição do valor à pagar final com ou sem desconto da categoria E
if categ.upper() == 'E' and qtd_psg < 2:
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {E*qtd_psg}')
elif categ.upper() == 'E' and qtd_psg == 2:
    descont = float((E * qtd_psg) - ((E * qtd_psg) * 0.04))
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {E*qtd_psg}, com o desconto de 3% passará para {descont}')
elif categ.upper() == 'E' and qtd_psg == 3:
    descont = float((E * qtd_psg) - ((E * qtd_psg) * 0.04))
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {E*qtd_psg}, com o desconto de 3% passará para {descont}')
elif categ.upper() == 'E' and qtd_psg >= 4:
    descont = float((E * qtd_psg) - ((E * qtd_psg) * 0.05))
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {E*qtd_psg}, com o desconto de 3% passará para {descont}')

#Exibição do valor à pagar final com ou sem desconto da categoria Ex
elif categ.upper() == 'EX' and qtd_psg < 2:
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {EX * qtd_psg}')
elif categ.upper() == 'EX' and qtd_psg == 2:
    descont = float((EX * qtd_psg) - ((EX * qtd_psg) * 0.05))
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {EX*qtd_psg}, com o desconto de 5% passará para {descont}')
elif categ.upper() == 'EX' and qtd_psg == 3:
    descont = float((EX * qtd_psg) - ((EX * qtd_psg) * 0.07))
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {EX*qtd_psg}, com o desconto de 7% passará para {descont}')
elif categ.upper() == 'EX' and qtd_psg >= 4:
    descont = float((EX * qtd_psg) - ((EX * qtd_psg) * 0.08))
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {EX*qtd_psg}, com o desconto de 8% passará para {descont}')

#Exibição do valor à pagar final com ou sem desconto da categoria PC
elif categ.upper() == 'PC' and qtd_psg < 2:
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {PC*qtd_psg}')
elif categ.upper() == 'PC' and qtd_psg == 2:
    descont = float((PC * qtd_psg) - ((PC * qtd_psg) * 0.10))
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {PC*qtd_psg}, com o desconto de 10% passará para {descont}')
elif categ.upper() == 'PC' and qtd_psg == 3:
    descont = float((PC * qtd_psg) - ((PC * qtd_psg) * 0.15))
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {PC*qtd_psg}, com o desconto de 15% passará para {descont}')
elif categ.upper() == 'PC' and qtd_psg >= 4:
    descont = float((PC * qtd_psg) - ((PC * qtd_psg) * 0.20))
    print(f'Seu voo na categoria {categ.upper()} ficará no valor de {PC*qtd_psg}, com o desconto de 20% passará para {descont}')