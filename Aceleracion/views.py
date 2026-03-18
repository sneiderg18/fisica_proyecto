from django.shortcuts import render


class TiempoNegativoError(Exception):
    pass


def validar_tiempo(t):
    return TiempoNegativoError() if t < 0 else None


def lanzar_si_error(e):
    if e:
        raise e


def index(request):
    return render(request, 'Aceleracion/index.html')


def aceleracion(request):
    resultado = None
    error = None
    variable_resuelta = None

    formulas = {
        'a':  (['vf', 'vi', 't'], lambda vf, vi, t, **_: (lanzar_si_error(validar_tiempo(t)), (vf - vi) / t)[1],  "Aceleración (m/s²)"),
        'vf': (['vi', 'a', 't'],  lambda vi, a, t, **_:  (lanzar_si_error(validar_tiempo(t)), vi + a * t)[1],      "Velocidad final (m/s)"),
        'vi': (['vf', 'a', 't'],  lambda vf, a, t, **_:  (lanzar_si_error(validar_tiempo(t)), vf - a * t)[1],      "Velocidad inicial (m/s)"),
        't':  (['vf', 'vi', 'a'], lambda vf, vi, a, **_: (vf - vi) / a,                                            "Tiempo (s)"),
    }

    try:
        buscar = request.POST.get('buscar')
        campos, formula, nombre = formulas[buscar]
        valores = {campo: float(request.POST.get(campo, '')) for campo in campos}
        resultado = formula(**valores)
        variable_resuelta = nombre

    except TiempoNegativoError:
        error = "El tiempo no puede ser negativo."
    except ZeroDivisionError:
        error = "El divisor no puede ser cero."
    except (TypeError, ValueError, KeyError):
        pass

    return render(request, 'Aceleracion/aceleracion.html', {
        'resultado': resultado,
        'error': error,
        'variable_resuelta': variable_resuelta,
        'post': request.POST,
    })


def posicion(request):
    resultado = None
    error = None
    variable_resuelta = None

    formulas = {
        'x':  (['x0', 'v', 't'], lambda x0, v, t, **_: (lanzar_si_error(validar_tiempo(t)), x0 + v * t)[1],   "Posición final (m)"),
        'x0': (['x', 'v', 't'],  lambda x, v, t, **_:  (lanzar_si_error(validar_tiempo(t)), x - v * t)[1],    "Posición inicial (m)"),
        'v':  (['x', 'x0', 't'], lambda x, x0, t, **_: (lanzar_si_error(validar_tiempo(t)), (x - x0) / t)[1], "Velocidad (m/s)"),
        't':  (['x', 'x0', 'v'], lambda x, x0, v, **_: (x - x0) / v,                                          "Tiempo (s)"),
    }

    try:
        buscar = request.POST.get('buscar')
        campos, formula, nombre = formulas[buscar]
        valores = {campo: float(request.POST.get(campo, '')) for campo in campos}
        resultado = formula(**valores)
        variable_resuelta = nombre

    except TiempoNegativoError:
        error = "El tiempo no puede ser negativo."
    except ZeroDivisionError:
        error = "El divisor no puede ser cero."
    except (TypeError, ValueError, KeyError):
        pass

    return render(request, 'Aceleracion/posicion.html', {
        'resultado': resultado,
        'error': error,
        'variable_resuelta': variable_resuelta,
        'post': request.POST,
    })