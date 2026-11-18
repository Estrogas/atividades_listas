L = []
maior_num = 0
menor_num = 999999
while True:
    opcao = int(input('Digite 1 para adicionar um número a lista\nDigite 2 para sair: '))
    if opcao == 1:
        numero = int(input('Digite um número: '))
        L.append (numero)
        if numero > maior_num:
            maior_num = numero
        if numero < menor_num:
            menor_num = numero
    elif opcao == 2:
        break
    else:
        print('Inválido')
media_geo = (maior_num * menor_num)**(1/2)
print(f'A média geométrica entre {maior_num} e {menor_num} é: {media_geo}')
