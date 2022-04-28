import time
import random
lista = []
jogos = []
print('-'*30)
print('   JOGA NA MEGA SENA   ')
print('-'*30)
quant = int(input('Quantos jogos você quer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('{:-^40}'.format(f'SORTEANDO {quant} JOGOS'))
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)
print('=-'*5,'< BOA SORTE! >','=-'*5)