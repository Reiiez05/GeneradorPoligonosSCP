def guardar_coordenadas_txt(coordenadas, ruta_salida):
    """
    Guarda las coordenadas en un archivo TXT.
    Cada línea tendrá el formato:

    longitud,latitud
    """

    with open(ruta_salida, "w", encoding="utf-8") as archivo:

        for coordenada in coordenadas:
            archivo.write(f"{coordenada}\n")