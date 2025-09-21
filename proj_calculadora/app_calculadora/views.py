from django.shortcuts import render
from .utils.decimal_para_binario import decimalBinario
from .utils.binario_para_decimal import binarioDecimal
from .utils.decimal_para_hexadecimal import decimalHexadecimal
from .utils.hexadecimal_para_decimal import hexadecimalDecimal
from django.contrib import messages


def inicio(request):
    decimal = binario = hexadecimal = dado_decimal = dado_binario = dado_hexadecimal = None

    if request.method == 'POST': # receber os dados do formulário (PoST)
        dado_decimal = str(request.POST.get('decimal'))

        # se não possuir dados no input do decimal: 

        if not dado_decimal: # se o input de decimal não tiver nenhum valor
            dado_binario = str(request.POST.get('binario'))

            # se não possuir dados no input do binário:
            if not dado_binario:
                dado_hexadecimal = str(request.POST.get('hexadecimal'))

                hexadecimal = dado_hexadecimal
                decimal = hexadecimalDecimal(dado_hexadecimal) # possui dados no input hexadecimal
                binario = decimalBinario(decimal)


            else:
                binario = dado_binario
                decimal = binarioDecimal(binario, decimal=0) # possui dados no input binário
                hexadecimal = decimalHexadecimal(int(decimal)) 

        else:
            decimal = dado_decimal
            binario = decimalBinario(int(dado_decimal))
            hexadecimal = decimalHexadecimal(int(dado_decimal)) # possui dados no input decimal
    
    contexto = {
        "decimal": decimal,
        "binario": binario,
        "hexadecimal": hexadecimal
    }
    return render(request, 'inicio.html', contexto)
