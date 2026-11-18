import random
rifa=[]
while True:
    opcao = int(input('Digite 1 para adicionar um participante a rifa\nDigite 2 para sair: '))
    if opcao == 1:
        rifa.append(input('Digite o nome do participante: '))
    elif opcao == 2:
        break
    else:
        print('Digite uma opcao válida')
sorteado = random.choice(rifa)
print(f'O ganhador da rifa foi: {sorteado}')