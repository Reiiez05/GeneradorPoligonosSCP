from config import *

from src.io.lector_kml import cargar_kml
from src.geometry.proyeccion_utm import obtener_crs_utm
from src.geometry.transformador import transformar_a_utm
from src.geometry.bufferizador import generar_buffer
from src.geometry.limpiador import limpiar_poligono
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

print("Limpiando geometría...")

poligono = limpiar_poligono(poligono)

print("Exportando...")

exportar_poligono(
    poligono,
    gdf.crs,
    OUTPUT_KML
)

print(f"Proceso finalizado: {OUTPUT_KML}")