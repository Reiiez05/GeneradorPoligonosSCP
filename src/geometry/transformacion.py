import geopandas as gpd


def transformar_a_utm(gdf, crs_utm):
    """
    Convierte el GeoDataFrame al sistema de coordenadas UTM.
    """

    return gdf.to_crs(crs_utm)