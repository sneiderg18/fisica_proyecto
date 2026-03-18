from django.shortcuts import render

def index(request):
    return render(request, 'Aceleracion/index.html')


def aceleracion(request):
    resultado = None
    error = None
    variable_resuelta = None

    formulas = {
        'a':  (['vf', 'vi', 't'], lambda vf, vi, t, **_: (vf - vi) / t,  "Aceleración (m/s²)"),
        'vf': (['vi', 'a', 't'],  lambda vi, a, t, **_:  vi + a * t,      "Velocidad final (m/s)"),
        'vi': (['vf', 'a', 't'],  lambda vf, a, t, **_:  vf - a * t,      "Velocidad inicial (m/s)"),
        't':  (['vf', 'vi', 'a'], lambda vf, vi, a, **_: (vf - vi) / a,   "Tiempo (s)"),
    }

    try:
        buscar = request.POST.get('buscar')
        campos, formula, nombre = formulas[buscar]
        valores = {campo: float(request.POST.get(campo, '')) for campo in campos}
        resultado = formula(**valores)
        variable_resuelta = nombre

    except ZeroDivisionError:
        error = "El divisor no puede ser cero."
    except (TypeError, ValueError, KeyError):
        pass

    return render(request, 'Aceleracion/aceleracion.html', {
        'resultado': resultado,
        'error': error,
        'variable_resuelta': variable_resuelta,
    })


def posicion(request):
    resultado = None
    error = None
    variable_resuelta = None

    formulas = {
        'x':  (['x0', 'v', 't'], lambda x0, v, t, **_:  x0 + v * t,   "Posición final (m)"),
        'x0': (['x', 'v', 't'],  lambda x, v, t, **_:   x - v * t,     "Posición inicial (m)"),
        'v':  (['x', 'x0', 't'], lambda x, x0, t, **_:  (x - x0) / t,  "Velocidad (m/s)"),
        't':  (['x', 'x0', 'v'], lambda x, x0, v, **_:  (x - x0) / v,  "Tiempo (s)"),
    }

    try:
        buscar = request.POST.get('buscar')
        campos, formula, nombre = formulas[buscar]
        valores = {campo: float(request.POST.get(campo, '')) for campo in campos}
        resultado = formula(**valores)
        variable_resuelta = nombre

    except ZeroDivisionError:
        error = "El divisor no puede ser cero."
    except (TypeError, ValueError, KeyError):
        pass

    return render(request, 'Aceleracion/posicion.html', {
        'resultado': resultado,
        'error': error,
        'variable_resuelta': variable_resuelta,
    })