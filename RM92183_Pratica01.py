# Variáveis necessárias: BPM e Idade

idade = int(input('Informe sua idade: '))
BPM = int(input('Informe seus Batimentos Por Minuto (BPM): '))

if idade <= 2 and BPM < 120:
    print('Seus batimentos cardíacos estão ABAIXO da faixa adequada')
elif idade <= 2 and BPM >= 120 and BPM <= 140:
    print('Seus batimentos cardíacos estão DENTRO da faixa adequada')
elif idade <= 2 and BPM > 140:
    print('Seus batimentos cardíacos estão ACIMA da faixa adequada')
elif idade >= 8 and idade <= 17 and BPM < 80:
    print('Seus batimentos cardíacos estão ABAIXO da faixa adequada')
elif idade >= 8 and idade <= 17 and BPM >= 80 and BPM <= 100:
    print('Seus batimentos cardíacos estão DENTRO da faixa adequada')
elif idade >= 8 and idade <= 17 and BPM > 100:
    print('Seus batimentos cardíacos estão ACIMA da faixa adequada')
elif idade >= 18 and idade <= 65 and BPM < 70:
    print('Seus batimentos cardíacos estão ABAIXO da faixa adequada')
elif idade >= 18 and idade <= 65 and BPM >= 70 and BPM <= 80:
    print('Seus batimentos cardíacos estão DENTRO da faixa adequada')
elif idade >= 18 and idade <= 65 and BPM > 80:
    print('Seus batimentos cardíacos estão ACIMA da faixa adequada')
elif idade > 65 and BPM < 50:
    print('Seus batimentos cardíacos estão ABAIXO da faixa adequada')
elif idade > 65 and BPM >= 50 and BPM <= 60:
    print('Seus batimentos cardíacos estão DENTRO da faixa adequada')
else:
    idade > 65 and BPM > 60
    print('Seus batimentos cardíacos estão ACIMA da faixa adequada')
