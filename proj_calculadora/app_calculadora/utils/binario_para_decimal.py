# Tendo em vista que todos os computadores trabalham na base binária e nós utilizamos usualmente a base decimal, faz-se necessário saber converter binário para decimal e vice-versa. 

# a função recebe como entrada strings
def binarioDecimal(binario, lista_binario = None, decimal = 0):
    if lista_binario is None: # evita reutilizar a lista, evitando a soma dos valores
        lista_binario = []

    c = 0
    for elementos in binario:
        lista_binario.append(elementos)    

    lista_binario.reverse()
    for b in lista_binario:
        numero = int(b)
        decimal += (numero * 2 ** c)
        
        c+= 1

    return str(decimal)


# if __name__ == '__main__':
#     binario = str(input())
#     print(binarioDecimal(binario))
#     print(type(binarioDecimal(binario)))