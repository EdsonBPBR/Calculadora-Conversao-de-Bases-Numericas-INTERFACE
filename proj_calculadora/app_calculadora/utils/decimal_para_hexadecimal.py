# conversão de um número decimal para um número hexadecimal

# # a função recebe como entrada números inteiros
def decimalHexadecimal(decimal):
    lista_hexadecimal = []
    str_hexadecimal = ''

    base_reversa = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
    }

    while True:
        if (decimal % 16) > 9:
            lista_hexadecimal.append(base_reversa[(decimal % 16)])  
        else:
            lista_hexadecimal.append((decimal % 16))
            
        decimal = decimal // 16

        if decimal == 0:
            break

    lista_hexadecimal.reverse()

    for elemento in lista_hexadecimal:
        str_hexadecimal += f'{elemento}'

    return str_hexadecimal

# decimal = 2569
# print(decimalHexadecimal(decimal))