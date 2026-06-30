from shapely.geometry import Polygon


def simplificar_douglas(poligono, tolerancia):
    """
    Simplifica un polígono manteniendo la topología.
    """

    return poligono.simplify(
        tolerance=tolerancia,
        preserve_topology=True
    )


def contar_vertices(poligono):
    """
    Devuelve el número de vértices del contorno exterior.
    """

    if poligono.geom_type != "Polygon":
        raise TypeError("La geometría debe ser Polygon")

    return len(poligono.exterior.coords)