from config import *

from src.io.lector_kml import cargar_kml
from src.geometry.proyeccion_utm import obtener_crs_utm
from src.geometry.transformador import (
    transformar_a_utm,
    geometria_a_wgs84
)
from src.geometry.bufferizador import generar_buffer
from src.geometry.limpiador import limpiar_poligono
from src.geometry.validador import validar_geometria
from src.geometry.removedor_huecos import eliminar_huecos
from src.io.exportador import exportar_poligono


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

print("Validando geometría...")

poligono = validar_geometria(poligono)

print("Limpiando geometría...")

poligono = limpiar_poligono(poligono)

print("Eliminando huecos...")

poligono = eliminar_huecos(poligono)

print("Regresando a WGS84...")

poligono = geometria_a_wgs84(
    poligono,
    gdf_utm.crs
)

print("Exportando...")

exportar_poligono(
    poligono,
    OUTPUT_KML
)

print("===================================")
print("Proceso finalizado correctamente")
print(f"Archivo generado: {OUTPUT_KML}")
print(f"Geometría válida: {poligono.is_valid}")
print(f"Tipo: {poligono.geom_type}")
print("===================================")