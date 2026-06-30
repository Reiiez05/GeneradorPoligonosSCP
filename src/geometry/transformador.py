import geopandas as gpd


def transformar_a_utm(gdf, crs_utm):
    """
    Convierte el GeoDataFrame al sistema UTM.
    """
    return gdf.to_crs(crs_utm)


def geometria_a_wgs84(geometria, crs_origen):
    """
    Convierte una geometría Shapely desde UTM a WGS84.
    """

    gdf = gpd.GeoDataFrame(
        geometry=[geometria],
        crs=crs_origen
    )

    gdf = gdf.to_crs(epsg=4326)

    return gdf.geometry.iloc[0]