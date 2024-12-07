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
    vals = []
    for v in datos:
        if math.isfinite(v):
            vals.append(v)
	# Ordenar lista
    vals.sort()

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

# prueba
if __name__ == "__main__":
    vals_in = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Promedio:", promedio_cal(vals_in))
    print("Mediana:", mediana_cal(vals_in))
    print("Moda:", moda_cal(vals_in))
    print("Rango:", rango_cal(vals_in))
    print("Varianza:", varianza_cal(vals_in))
    print("Desviación estándar:", STD_cal(vals_in))
    print("Cuartiles (Q1, Q2, Q3):", percentil_cal(vals_in, 25), percentil_cal(vals_in, 50), percentil_cal(vals_in, 75))
    print("Rango intercuartílico:", IQR_cal(vals_in))
    print("Desviación mediana absoluta:", MAD_calc(vals_in))
