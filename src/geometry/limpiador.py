from shapely.geometry import MultiPolygon


def limpiar_poligono(poligono):
    """
    Limpia la geometría resultante del buffer.

    - Si existe un MultiPolygon,
      conserva únicamente el polígono más grande.
    """

    if isinstance(poligono, MultiPolygon):
        poligono = max(
            poligono.geoms,
            key=lambda p: p.area
        )

    return poligono