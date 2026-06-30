from shapely.ops import unary_union


def generar_buffer(gdf_utm, distancia):
    """
    Genera un buffer sobre todas las líneas y las une en una sola geometría.

    distancia = metros
    """

    buffer = gdf_utm.buffer(distancia)

    poligono = unary_union(buffer)

    return poligono