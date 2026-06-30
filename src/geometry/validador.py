from shapely.validation import make_valid


def validar_geometria(geometria):
    """
    Corrige geometrías inválidas antes de continuar
    con el procesamiento.
    """

    if not geometria.is_valid:
        geometria = make_valid(geometria)

    return geometria