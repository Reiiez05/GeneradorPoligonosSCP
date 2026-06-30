import geopandas as gpd


def exportar_poligono(poligono, ruta_salida):
    """
    Exporta un Polygon a un archivo KML.
    La geometría debe venir ya en WGS84.
    """

    gdf = gpd.GeoDataFrame(
        geometry=[poligono],
        crs="EPSG:4326"
    )

    gdf.to_file(
        ruta_salida,
        driver="KML"
    )