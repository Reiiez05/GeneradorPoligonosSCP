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
from src.export.coordenadas import (
    extraer_coordenadas,
    formatear_coordenadas_scp
)
from src.export.txt import guardar_coordenadas_txt
from src.export.wkt import generar_wkt, generar_wkt_punto
from src.export.sql import generar_insert_sql
from src.export.archivo import guardar_archivo


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

coordenadas = extraer_coordenadas(poligono)
coordenadas_scp = formatear_coordenadas_scp(
    coordenadas
)

print(f"Total de coordenadas: {len(coordenadas_scp)}")
    
guardar_coordenadas_txt(
    coordenadas_scp,
    "output/coordenadas_scp.txt"
)

wkt = generar_wkt(poligono)
wkt_punto = generar_wkt_punto(poligono)

sql = generar_insert_sql(
    nombre="PRUEBA",
    descripcion="Generado desde Python",
    wkt_poligono=wkt,
    wkt_punto=wkt_punto,
    zona_padre=None
)

guardar_archivo(
    wkt,
    "output/geocerca.wkt"
)

guardar_archivo(
    wkt_punto,
    "output/centro.wkt"
)

guardar_archivo(
    sql,
    "output/insertar_zona.sql"
)

print("\n===================================")
print("ARCHIVOS GENERADOS")
print("===================================")

print("✓ buffer20m.kml")
print("✓ coordenadas_scp.txt")
print("✓ geocerca.wkt")
print("✓ centro.wkt")
print("✓ insertar_zona.sql")