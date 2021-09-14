notas = []
x = 0
while len(notas) < 4:
    x = float(input('Digite suas 4 notas: '))
    if x >= 0 and x <= 10:
        notas.append(x)
    else:
        print('Digite uma nota possível')

media = sum(notas)/4

if media == 0:
    resultado = 'reprovado'
elif media < 3.9:
    resultado = 'Reprovado mas não zerado'
elif media < 6:
    resultado = 'Em recuperação'
else:
    resultado = 'Aprovado'

for i in range(0, 4):
    print(f'|{notas[i]}', end = '')
print('| →', media, '→', resultado)