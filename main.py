from src.lector_kml import cargar_kml
from src.geometry.proyeccion import obtener_crs_utm
from src.geometry.transformacion import transformar_a_utm

RUTA_KML = "input/REGION I XICOTEPEC.kml"

gdf = cargar_kml(RUTA_KML)

crs_utm = obtener_crs_utm(gdf)

gdf_utm = transformar_a_utm(gdf, crs_utm)

print(f"CRS original : {gdf.crs}")
print(f"CRS UTM      : {gdf_utm.crs}")

print("\nPrimer punto original:")
print(gdf.geometry.iloc[0])

print("\nPrimer punto en UTM:")
print(gdf_utm.geometry.iloc[0])