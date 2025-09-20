from django.shortcuts import render
from .utils.decimal_para_binario import decimalBinario
from django.contrib import messages


def inicio(request):

    if request.method == 'POST': # receber os dados do formulário (PoST)
        dado_decimal = str(request.POST.get('decimal'))

        if not dado_decimal: # se o input de decimal não tiver nenhum valor
            dado_binario = str(request.POST.get('binario'))
            



        else:
            binario = decimalBinario(int(dado_decimal))
            decimal = dado_decimal
    
    elif request.method == 'GET': # obter (a página já carrega em get)
        dado_decimal = None 

    contexto = {
        "decimal": decimal,
        "binario": binario
    }
    return render(request, 'inicio.html', contexto)
