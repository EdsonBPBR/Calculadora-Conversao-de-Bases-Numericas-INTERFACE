# converter hexadecimal para decimal

# a função recebe como entrada strings
def hexadecimalDecimal(hexadecimal):
    lista_hexadecimal = list(hexadecimal)
    lista_hexadecimal.reverse()

    bases = {
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15
    }

    decimal = 0
    c = 0
    
    for elemento in lista_hexadecimal:
        if elemento == 'A' or elemento == 'B' or elemento == 'C' or elemento == 'D' or elemento == 'E' or elemento == 'F':
            decimal += bases[elemento] * 16 ** c
        else:
            decimal += int(elemento) * 16 ** c
        c += 1
        
    return decimal

# hexa = 'FFF'
# print(hexadecimalDecimal(hexa))