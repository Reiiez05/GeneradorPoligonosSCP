def guardar_archivo(texto, ruta_salida):
    """
    Guarda un texto en un archivo.
    """

    with open(
        ruta_salida,
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.write(texto)