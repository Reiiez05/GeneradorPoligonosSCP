from pyproj import CRS


def obtener_crs_utm(gdf):
    """
    Detecta automáticamente la zona UTM adecuada
    tomando el centro del GeoDataFrame.
    """

    xmin, ymin, xmax, ymax = gdf.total_bounds

    longitud = (xmin + xmax) / 2
    latitud = (ymin + ymax) / 2

    zona = int((longitud + 180) / 6) + 1

    if latitud >= 0:
        epsg = 32600 + zona
    else:
        epsg = 32700 + zona

    return CRS.from_epsg(epsg)