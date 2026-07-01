def generar_wkt(poligono):
    """
    Convierte un Polygon de Shapely
    al formato WKT requerido por
    SQL Server Geography.
    """

    coordenadas = []

    for lon, lat in poligono.exterior.coords:
        coordenadas.append(f"{lon} {lat}")

    texto = ",\n".join(coordenadas)

    return f"POLYGON(({texto}))"

def generar_wkt_punto(poligono):
    """
    Genera el WKT del centroide del polígono.
    """

    centro = poligono.centroid

    return f"POINT ({centro.x} {centro.y})"