def extraer_coordenadas(poligono):
    """
    Extrae las coordenadas del contorno exterior
    del polígono.
    """

    return list(poligono.exterior.coords)


def formatear_coordenadas_scp(coordenadas):
    """
    Convierte las coordenadas al formato utilizado
    por SCP.

    Retorna una lista de cadenas:
    longitud,latitud
    """

    resultado = []

    for lon, lat in coordenadas:
        resultado.append(f"{lon},{lat}")

    return resultado