from django.shortcuts import render
from .utils.decimal_para_binario import decimalBinario
from .utils.binario_para_decimal import binarioDecimal
from .utils.decimal_para_hexadecimal import decimalHexadecimal
from .utils.hexadecimal_para_decimal import hexadecimalDecimal
from .utils.octal_para_decimal import octalDecimal
from .utils.decimal_para_octal import decimalOctal
from django.contrib import messages


def inicio(request):
    decimal = binario = hexadecimal = octal = dado_decimal = dado_binario = dado_hexadecimal = dado_octal = None # é necessário pq a primeira requisição HTML realizada é o GET, senão dá erro 

    if request.method == 'POST': # receber os dados do formulário (PoST)
        dado_decimal = str(request.POST.get('decimal'))

        # se não possuir dados no input do decimal: 
        if not dado_decimal: # se o input de decimal não tiver nenhum valor
            dado_binario = str(request.POST.get('binario'))

            # se não possuir dados no input do binário:
            if not dado_binario:
                dado_hexadecimal = str(request.POST.get('hexadecimal')).upper()

                # se não possuir dados no input do hexadecimal:
                if not dado_hexadecimal:
                    dado_octal = str(request.POST.get('octal'))
                    
                    if not dado_octal:
                        messages.error(request, 'É necessário inserir UM DADO em uma das ENTRADAS!')


                    octal = dado_octal
                    decimal = octalDecimal(dado_octal)
                    binario = decimalBinario(decimal)
                    hexadecimal = decimalHexadecimal(decimal)
                
                else:
                    hexadecimal = dado_hexadecimal
                    decimal = hexadecimalDecimal(dado_hexadecimal) # possui dados no input hexadecimal
                    binario = decimalBinario(decimal)
                    octal = decimalOctal(decimal)

            else:
                binario = dado_binario
                decimal = binarioDecimal(binario, decimal=0) # possui dados no input binário
                hexadecimal = decimalHexadecimal(int(decimal)) 
                octal = decimalOctal(int(decimal))

        else:
            decimal = dado_decimal
            binario = decimalBinario(int(dado_decimal))
            hexadecimal = decimalHexadecimal(int(dado_decimal)) # possui dados no input decimal
            octal = decimalOctal(int(dado_decimal))
    
    if decimal == binario == hexadecimal == octal == None:
        decimal = binario = hexadecimal = octal = ''

    contexto = {
        "decimal": decimal,
        "binario": binario,
        "hexadecimal": hexadecimal,
        "octal": octal
    }

    return render(request, 'inicio.html', contexto)
