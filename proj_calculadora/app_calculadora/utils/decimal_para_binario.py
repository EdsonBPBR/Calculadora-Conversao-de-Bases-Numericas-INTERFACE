# Dado um número n na base decimal, escreva uma função recursiva que converte este número para binário. 

# a função recebe como entrada números inteiros
def decimalBinario(decimal):
    binario = []
    c = decimal
    str_binario = ''
    while True:
        binario.append(c % 2)
        c = c // 2
        if c == 0:
            break
        
    binario.reverse()
    for elemento in binario:
        str_binario += f'{elemento}'

    return str_binario

# decimal = int(input())
# print(decimalBinario(decimal))