# conversão de um número decimal para um número octal

# a função recebe como entrada números inteiros
def decimalOctal(decimal):
    octal = []
    string_octal = ''
    
    resultado = decimal
    while True:
        octal.append(resultado % 8)
        resultado = resultado // 8
        
        if resultado == 0:
            break
        
    octal.reverse()

    for elemento in octal:
        string_octal += f'{elemento}'

    return string_octal



    
    