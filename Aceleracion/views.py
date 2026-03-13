from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request, 'Aceleracion/index.html')

def aceleracion (request):

    resultado = None
    error = None

    if request.method == 'POST':
        try:
            vf = float(request.POST.get('vf'))
            vi = float(request.POST.get('vi'))
            t = float(request.POST.get('t'))

            if t == 0:
                error = "El tiempo no puede ser cero."
            else:
                resultado = (vf - vi) / t

        except (TypeError, ValueError):
            error = "Ingresa valores numericos validos."

             
    return render (request, 'Aceleracion/aceleracion.html', {
        'resultado': resultado,
        'error': error,
    })



def posicion (request):

    resultado = None
    error = None

    if request.method == 'POST':
        try:
            x0 = float(request.POST.get('x0'))
            v = float(request.POST.get('v'))
            t = float(request.POST.get('t'))

            resultado = x0 + v * t

        except (TypeError, ValueError):
            error = "Ingresa valores validos"


    return render (request, 'Aceleracion/posicion.html', {
        'resultado': resultado,
        'error': error,
    })