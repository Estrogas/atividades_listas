lista=[]
palavra=''
caracteres = 0
for i in range(5):
    p = input('Digite uma palavra: ')
    lista.append(p)
    c=len(p)
    if c>caracteres:
        caracteres=c
        palavra=p
print(f'A palavra que tem maior numero de caracteres é: {palavra}')