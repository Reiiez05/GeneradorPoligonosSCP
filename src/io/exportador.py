import geopandas as gpd


def exportar_poligono(poligono, crs, ruta_salida):

    gdf = gpd.GeoDataFrame(
        geometry=[poligono],
        crs=crs
    )

    gdf.to_file(
        ruta_salida,
        driver="KML"
    )