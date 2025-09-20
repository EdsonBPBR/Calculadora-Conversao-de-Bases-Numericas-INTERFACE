from django.shortcuts import render
from .utils.decimal_para_binario import decimalBinario
from .utils.binario_para_decimal import binarioDecimal
from django.contrib import messages


def inicio(request):
    decimal = binario = dado_decimal =  dado_binario = None

    if request.method == 'POST': # receber os dados do formulário (PoST)
        dado_decimal = str(request.POST.get('decimal'))

        if not dado_decimal: # se o input de decimal não tiver nenhum valor
            dado_binario = str(request.POST.get('binario'))
            binario = dado_binario
            decimal = binarioDecimal(binario, decimal=0)

        else:
            binario = decimalBinario(int(dado_decimal))
            decimal = dado_decimal
    

    contexto = {
        "decimal": decimal,
        "binario": binario,
    }
    return render(request, 'inicio.html', contexto)
