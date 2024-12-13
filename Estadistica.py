import math
# Vals in en todo permite sacar valores que sean NaN
# Promedio aritmético
def promedio_cal(vals_in):
    """
    Calcula el promedio aritmético de una lista de vals_in.
    
    Parámetros:
        vals_in (list): Lista de números.
    
    Retorna:
        float: Promedio de los números en la lista.
    """
    # Eliminamos los valores que sean NaNs
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
	# Ordenar lista
    vals.sort()
    return sum(vals) / len(vals)

# Mediana
def mediana_cal(vals_in):
    """
    Calcula la mediana de una lista de vals_in.
    
    Parámetros:
        vals_in (list): Lista de números.
    
    Retorna:
        float: Mediana de los números en la lista.
    """
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
	# Ordenar lista
    vals.sort()

    n = len(vals_in)
    if n % 2 == 0:  # Número par de elementos
        return (vals[n // 2 - 1] + vals[n // 2]) / 2
    else:  # Número impar de elementos
        return vals[n // 2]

# Moda
def moda_cal(datos):
    """
    Calcula la moda de una lista de datos.
    Si todos los elementos tienen la misma frecuencia, indica que no hay moda.
    
    Parámetros:
        datos (list): Lista de números.
    
    Retorna:
        int, float, list o str: Moda de los números en la lista o un mensaje indicando que no hay moda.
    """
    frecuencia = {}
    for x in datos:
        if x in frecuencia:
            frecuencia[x] += 1
        else:
            frecuencia[x] = 1
    max_frecuencia = max(frecuencia.values())
    modas = [elemento for elemento, frecuencia in frecuencia.items() if frecuencia == max_frecuencia]
    return modas

# Rango
def rango_cal(vals_in):
    """
    Calcula el rango (máximo - mínimo) de una lista de vals_in.
    
    Parámetros:
        vals_in (list): Lista de números.
    
    Retorna:
        float: Diferencia entre el valor máximo y mínimo.
    """
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
	# Ordenar lista
    vals.sort()

    return max(vals) - min(vals)

# Varianza
def varianza_cal(vals_in):
    """
    Calcula la varianza de una lista de vals_in.
    
    Parámetros:
        vals_in (list): Lista de números.
    
    Retorna:
        float: Varianza.
    """
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
	# Ordenar lista
    vals.sort()

    promedio = promedio_cal(vals)
    return sum((i - promedio) ** 2 for i in vals) / len(vals)

# Desviación estándar
def STD_cal(vals_in):
    """
    Calcula la desviación estándar muestral de una lista de vals_in.
    
    Parámetros:
        vals_in (list): Lista de números.
    
    Retorna:
        float: Desviación estándar muestral.
    """
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
	# Ordenar lista
    vals.sort()

    return math.sqrt(varianza_cal(vals))

# Percentiles
def percentil_cal(vals_in, percentil):
    """
    Calcula el percentil especificado de una lista de vals_in.
    
    Parámetros:
        vals_in (list): Lista de números.
        percentil (float): Percentil a calcular (0-100).
    
    Retorna:
        float: Valor del percentil.
    """
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)

    # Ordenar lista
    vals.sort()

    k = (len(vals) - 1) * (percentil / 100)
    f = int(k)  # Parte entera
    c = k - f   # Parte decimal
    if f + 1 < len(vals):
        return vals[f] + c * (vals[f + 1] - vals[f])
    else:
        return vals[f]

# Rango intercuartílico
def IQR_cal(vals_in):
    """
    Calcula el rango intercuartílico (Q3 - Q1) de una lista de vals_in.
    
    Parámetros:
        vals_in (list): Lista de números.
    
    Retorna:
        float: Rango intercuartílico.
    """
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
	# Ordenar lista
    vals.sort()

    q1 = percentil_cal(vals, 25)
    q3 = percentil_cal(vals, 75)
    return q3 - q1

# Desviación mediana absoluta
def MAD_calc(vals_in):
    """
    Calcula la desviación mediana absoluta de una lista de vals_in.
    
    Parámetros:
        vals_in (list): Lista de números.
    
    Retorna:
        float: Desviación mediana absoluta.
    """
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
	# Ordenar lista
    vals.sort()

    mediana = mediana_cal(vals)
    desviaciones = [abs(x - mediana) for x in vals]
    return mediana_cal(desviaciones)

def covar_cal(x_vals,y_vals):
    """
    Calcula la covarianza de listas (x_vals,y_vals)
    
    Parámetros:
        x_vals (list): números del eje x.
        y_vals (list): números del eje y.
    
    Retorna:
        float: Valor de la covarianza
    """
    x = []
    y = []
    for i in range(len(x_vals)):
        if math.isfinite(x_vals[i]) and math.isfinite(y_vals[i]):
            x.append(x_vals[i])
            y.append(y_vals[i])
    p_x = promedio_cal(x)
    p_y = promedio_cal(y)
    n = 0
    for i in range(len(x)):
        n += (x[i] - p_x) * (y[i] - p_y)
    
    covar_cal = n / (len(n))
    return covar_cal

def correlacion(x_vals,y_vals):
    '''
    Calcula el coeficiente de correlación de Pearson entre dos listas de valores.
    
    Parámetros:
        x_vals (list): valores para X.
        y_vals (list): valores para Y.
    
    Retorna:
        float: Coeficiente de correlación de Pearson.
    '''
    x = []
    y = []
    for i in range(len(x_vals)):
        if math.isfinite(x_vals[i]) and math.isfinite(y_vals[i]):
            x.append(x_vals[i])
            y.append(y_vals[i])
    cov = covar_cal(x, y)
    std_x = STD_cal(x)
    std_y = STD_cal(y)
    
    rxy = cov / (std_x * std_y)
    return rxy
