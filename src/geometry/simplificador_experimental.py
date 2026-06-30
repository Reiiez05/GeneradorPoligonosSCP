from simplification.cutil import simplify_coords
from shapely.geometry import Polygon


def simplificar_visvalingam(poligono, tolerancia):
    """
    Simplifica un polígono utilizando el algoritmo
    Visvalingam-Whyatt.

    Parámetros
    ----------
    poligono : Polygon
    tolerancia : float
        Valor de simplificación.

    Retorna
    -------
    Polygon
    """

    coords = list(poligono.exterior.coords)

    coords_simplificadas = simplify_coords(
        coords,
        tolerancia
    )

    return Polygon(coords_simplificadas)