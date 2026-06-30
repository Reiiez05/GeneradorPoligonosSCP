from config import *

from src.io.lector_kml import cargar_kml
from src.geometry.proyeccion_utm import obtener_crs_utm
from src.geometry.transformador import (
    transformar_a_utm,
    geometria_a_wgs84
)

from src.geometry.bufferizador import generar_buffer
from src.geometry.limpiador import limpiar_poligono
from src.geometry.removedor_huecos import eliminar_huecos

from src.geometry.simplificador_douglas import (
    simplificar_douglas,
    contar_vertices
)

from geometry.simplificador_experimental import (
    simplificar_visvalingam
)

from src.io.exportador import exportar_poligono


# ==========================================================
# CONFIGURACIÓN DEL BENCHMARK
# ==========================================================

METODO = "douglas"
# METODO = "visvalingam"

TOLERANCIAS = [
    50,
    75,
    100,
    125,
    150,
    200,
    250,
    300
]

EXPORTAR_TOLERANCIAS = [50, 100, 150]

# ==========================================================

print("Preparando geometría...\n")
print(f"Método de simplificación: {METODO}\n")

gdf = cargar_kml(INPUT_KML)

crs = obtener_crs_utm(gdf)

gdf_utm = transformar_a_utm(
    gdf,
    crs
)

poligono = generar_buffer(
    gdf_utm,
    BUFFER_METROS
)

poligono = limpiar_poligono(poligono)

poligono = eliminar_huecos(poligono)

vertices_originales = contar_vertices(poligono)

area_original = poligono.area

print(f"Vértices originales: {vertices_originales:,}")
print(f"Área original: {area_original:,.2f}\n")

print("==============================")
print("BANCO DE PRUEBAS")
print("==============================")

print(
    f"{'Tol.':>6} "
    f"{'Vertices':>12} "
    f"{'Reducción':>12} "
    f"{'Área':>15} "
    f"{'% Área':>10}"
)

print("-" * 65)

for tolerancia in TOLERANCIAS:

    if METODO == "douglas":

        poligono_simple = simplificar_douglas(
            poligono,
            tolerancia
        )

    elif METODO == "visvalingam":

        poligono_simple = simplificar_visvalingam(
            poligono,
            tolerancia
        )

    else:

        raise ValueError(
            f"Método de simplificación no soportado: {METODO}"
        )

    vertices = contar_vertices(poligono_simple)

    area = poligono_simple.area

    reduccion = (
        (vertices_originales - vertices)
        / vertices_originales
    ) * 100

    cambio_area = (
        (area - area_original)
        / area_original
    ) * 100

    print(
        f"{tolerancia:6}"
        f"{vertices:12,}"
        f"{reduccion:11.2f}%"
        f"{area:15,.2f}"
        f"{cambio_area:10.2f}%"
    )

    if tolerancia in EXPORTAR_TOLERANCIAS:

        print(f"   ↳ Generando KML {tolerancia} m...")

        poligono_exportar = geometria_a_wgs84(
            poligono_simple,
            crs
        )

        ruta_kml = f"output/poligono_{tolerancia}m.kml"

        exportar_poligono(
            poligono_exportar,
            ruta_kml
        )

        print(f"   ✓ {ruta_kml}")

print("\n==============================")
print("BENCHMARK FINALIZADO")
print("==============================")