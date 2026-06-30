import geopandas as gpd


def cargar_kml(ruta_archivo):
    """
    Lee el KML y conserva únicamente las geometrías tipo LineString.
    """

    gdf = gpd.read_file(ruta_archivo)

    if gdf.crs is None:
        gdf.set_crs(epsg=4326, inplace=True)

    # Conservar únicamente líneas
    gdf = gdf[gdf.geometry.geom_type == "LineString"]

    return gdf.reset_index(drop=True)