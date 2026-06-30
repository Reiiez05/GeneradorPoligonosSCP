from src.lector_kml import cargar_kml

RUTA_KML = "input/REGION I XICOTEPEC.kml"

gdf = cargar_kml(RUTA_KML)

print("===================================")
print("RESUMEN DEL KML")
print("===================================")

print(f"Total de rutas: {len(gdf)}")

print()

print("Tipos de geometría:")

print(gdf.geometry.geom_type.value_counts())

print()

print("Primeras rutas:")

print(gdf[["Name","geometry"]].head())