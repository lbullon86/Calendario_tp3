import calendar






def crea_lista_dias(fichero_dias_festivos):
    dias_festivos = fichero_dias_festivos.readline().strip()
    lista_dias_festivos = []

    if len(dias_festivos) > 0:
        lista_dias_festivos = dias_festivos.split(",")

    return lista_dias_festivos


def crea_calendario_festivos(ficheros_meses_festivos, fichero_dias_festivos):
    result = {}
    nombre_mes = ficheros_meses_festivos.readline().strip()

    lista_dias_festivos = crea_lista_dias(fichero_dias_festivos)

    while nombre_mes:

        result[nombre_mes] = lista_dias_festivos
        nombre_mes = ficheros_meses_festivos.readline().strip()
        lista_dias_festivos = crea_lista_dias(fichero_dias_festivos)

    return result

def consigue_primer_dia_year(year):
    # Controlar bisiestos
    if year == 2018:
        return 0
    else:
        return (year - 2018) % 7


def asignar_dias_semana(dias, primer_dia_mes):
    result = {}
    for dia in dias:
        result[dia] = primer_dia_mes
        primer_dia_mes = (primer_dia_mes + 1) % 7

    return result


def crea_calendario(fichero_meses, fichero_dias, primer_dia_mes):

    result = {}
    nombre_mes = fichero_meses.readline().strip()
    dias = fichero_dias.readline().strip().split(",")
    while nombre_mes:
        result[nombre_mes] = asignar_dias_semana(dias, primer_dia_mes)
        primer_dia_mes = (primer_dia_mes + len(dias)) % 7
        nombre_mes = fichero_meses.readline().strip()
        dias = fichero_dias.readline().strip().split(",")
    fichero_meses.close()
    fichero_dias.close()

    return result









