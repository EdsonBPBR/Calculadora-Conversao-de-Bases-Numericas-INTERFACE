# conversão de um número octal para um número decimal

## a função recebe como entrada strings
def octalDecimal(octal):
    lista_octal = list(octal)
    lista_octal.reverse()
    c = 0
    decimal = 0

    for elemento in lista_octal:
        elemento_inteiro = int(elemento)
        decimal += elemento_inteiro * 8 ** c
        c += 1

    return decimal

# octal = '755'
# print(octalDecimal(octal))