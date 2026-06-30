from config import *

from src.io.lector_kml import cargar_kml
from src.geometry.proyeccion_utm import obtener_crs_utm
from src.geometry.transformador import transformar_a_utm
from src.geometry.transformador import geometria_a_wgs84
from src.geometry.bufferizador import generar_buffer
from src.geometry.limpiador import limpiar_poligono
from src.io.exportador import exportar_poligono
from src.geometry.validador import validar_geometria


print("Leyendo KML...")

gdf = cargar_kml(INPUT_KML)

print("Transformando a UTM...")

gdf_utm = transformar_a_utm(
    gdf,
    obtener_crs_utm(gdf)
)

print("Generando buffer...")

poligono = generar_buffer(
    gdf_utm,
    BUFFER_METROS
)

poligono = validar_geometria(poligono)

poligono = limpiar_poligono(poligono)

print("Limpiando geometría...")

poligono = limpiar_poligono(poligono)

poligono = geometria_a_wgs84(
    poligono,
    gdf_utm.crs
)

print("Exportando...")

exportar_poligono(
    poligono,
    gdf.crs,
    OUTPUT_KML
)

print(f"Geometría válida: {poligono.is_valid}")
print(f"Tipo: {poligono.geom_type}")
