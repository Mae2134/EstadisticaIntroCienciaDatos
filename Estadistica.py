import math

# Promedio aritmético
def calcular_promedio(vals_in):
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
def calcular_mediana(vals_in):
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
def calcular_moda(datos):
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

    cuentas = {}
    
    for x in datos:
        if x in cuentas:
            cuentas[x] += 1
        else:
            cuentas[x] = 1
    
    max_frecuencia = max(cuentas.values())
    
    modas = [elemento for elemento, frecuencia in cuentas.items() if frecuencia == max_frecuencia]
    
    return modas

# Rango
def calcular_rango(vals_in):
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
def calcular_varianza(vals_in):
    """
    Calcula la varianza muestral de una lista de vals_in.
    
    Parámetros:
        vals_in (list): Lista de números.
    
    Retorna:
        float: Varianza muestral.
    """
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
	# Ordenar lista
    vals.sort()

    promedio = calcular_promedio(vals)
    return sum((x - promedio) ** 2 for x in vals) / (len(vals) - 1)

# Desviación estándar
def calcular_desviacion_estandar(vals_in):
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

    return math.sqrt(calcular_varianza(vals))

# Percentiles
def calcular_percentiles(vals_in, percentil):
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

    k = (len(vals_in) - 1) * (percentil / 100)
    f = int(k)  # Parte entera
    c = k - f   # Parte decimal
    if f + 1 < len(vals_in):
        return vals[f] + c * (vals[f + 1] - vals[f])
    else:
        return vals[f]

# Rango intercuartílico
def calcular_rango_intercuartilico(vals_in):
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

    q1 = calcular_percentiles(vals, 25)
    q3 = calcular_percentiles(vals, 75)
    return q3 - q1

# Desviación mediana absoluta
def calcular_desviacion_mediana_absoluta(vals_in):
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

    mediana = calcular_mediana(vals)
    desviaciones = [abs(x - mediana) for x in vals]
    return calcular_mediana(desviaciones)

# prueba
if __name__ == "__main__":
    vals_in = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Promedio:", calcular_promedio(vals_in))
    print("Mediana:", calcular_mediana(vals_in))
    print("Moda:", calcular_moda(vals_in))
    print("Rango:", calcular_rango(vals_in))
    print("Varianza:", calcular_varianza(vals_in))
    print("Desviación estándar:", calcular_desviacion_estandar(vals_in))
    print("Cuartiles (Q1, Q2, Q3):", calcular_percentiles(vals_in, 25), calcular_percentiles(vals_in, 50), calcular_percentiles(vals_in, 75))
    print("Rango intercuartílico:", calcular_rango_intercuartilico(vals_in))
    print("Desviación mediana absoluta:", calcular_desviacion_mediana_absoluta(vals_in))
