from shapely.geometry import Polygon


def eliminar_huecos(poligono):
    """
    Elimina todos los huecos interiores del polígono
    conservando únicamente el contorno exterior.
    """

    if poligono.geom_type != "Polygon":
        raise TypeError(
            f"Se esperaba Polygon y se recibió {poligono.geom_type}"
        )

    return Polygon(poligono.exterior)