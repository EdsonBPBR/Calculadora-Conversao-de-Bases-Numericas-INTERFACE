# Tendo em vista que todos os computadores trabalham na base binária e nós utilizamos usualmente a base decimal, faz-se necessário saber converter binário para decimal e vice-versa. 

# a função recebe como entrada strings
def binarioDecimal(binario, lista_binario = [], decimal = 0):
    c = 0
    for elementos in binario:
        lista_binario.append(elementos)    

    lista_binario.reverse()
    for b in lista_binario:
        numero = int(b)
        decimal += (numero * 2 ** c)
        
        c+= 1
    return decimal


