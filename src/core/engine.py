from config import *

# ==========================================
# Lectura / Escritura
# ==========================================
from src.io.lector_kml import cargar_kml
from src.io.exportador import exportar_poligono

# ==========================================
# Geometría
# ==========================================
from src.geometry.proyeccion_utm import obtener_crs_utm
from src.geometry.transformador import (
    transformar_a_utm,
    geometria_a_wgs84
)
from src.geometry.bufferizador import generar_buffer
from src.geometry.validador import validar_geometria
from src.geometry.limpiador import limpiar_poligono
from src.geometry.removedor_huecos import eliminar_huecos

# ==========================================
# Exportaciones
# ==========================================
from src.export.coordenadas import (
    extraer_coordenadas,
    formatear_coordenadas_scp
)
from src.export.txt import guardar_coordenadas_txt
from src.export.wkt import (
    generar_wkt,
    generar_wkt_punto
)
from src.export.sql import generar_insert_sql
from src.export.archivo import guardar_archivo


class GeneradorPoligonosEngine:

    def run(self):

        self._mostrar_encabezado()
        
        # ==========================================
        # Lectura y transformación
        # ==========================================

        gdf = cargar_kml(INPUT_KML)

        gdf_utm = transformar_a_utm(
            gdf,
            obtener_crs_utm(gdf)
        )

        poligono = self._procesar_geometria()        

def _mostrar_encabezado(self):

    print("========================================")
    print(" Generador de Polígonos SCP")
    print("========================================")
    print("Procesando archivo...\n")
    
# ==========================================
    # Procesamiento geométrico
# ==========================================

def _procesar_geometria(self):
        poligono = generar_buffer(
            gdf_utm,
            BUFFER_METROS
        )

        poligono = validar_geometria(poligono)

        poligono = limpiar_poligono(poligono)

        poligono = eliminar_huecos(poligono)

        poligono = geometria_a_wgs84(
            poligono,
            gdf_utm.crs
        )
        return poligono
    
# ==========================================
# Exportación KML
# ==========================================

def _generar_archivos(self, poligono):


        exportar_poligono(
            poligono,
            OUTPUT_KML
        )

# ==========================================
# Coordenadas SCP
# ==========================================

        coordenadas = extraer_coordenadas(poligono)

        coordenadas_scp = formatear_coordenadas_scp(
            coordenadas
        )

        guardar_coordenadas_txt(
            coordenadas_scp,
            OUTPUT_COORDENADAS
        )

# ==========================================
# WKT
# ==========================================

        wkt_poligono = generar_wkt(poligono)

        wkt_punto = generar_wkt_punto(poligono)

# ==========================================
# SQL
# ==========================================

        sql = generar_insert_sql(
            nombre=NOMBRE_ZONA,
            descripcion=DESCRIPCION_ZONA,
            wkt_poligono=wkt_poligono,
            wkt_punto=wkt_punto,
            zona_padre=None
        )

# ==========================================
# Guardado de archivos
# ==========================================

        guardar_archivo(
            wkt_poligono,
            OUTPUT_WKT
        )

        guardar_archivo(
            wkt_punto,
            OUTPUT_WKT_POINT
        )

        guardar_archivo(
            sql,
            OUTPUT_SQL
        )
        
        return {

    "poligono": poligono,
    "coordenadas": coordenadas_scp,
    "wkt": wkt_poligono,
    "wkt_point": wkt_punto,
    "sql": sql,
    "archivos": {

        "kml": OUTPUT_KML,
        "scp": OUTPUT_COORDENADAS,
        "wkt": OUTPUT_WKT,
        "point": OUTPUT_WKT_POINT,
        "sql": OUTPUT_SQL

    }

}

def _mostrar_resumen(self, resultado["archivos"]["kml"]):
    
# ==========================================
# Resumen
# ==========================================

        print("Proceso finalizado correctamente.\n")

        print("Archivos generados:")

        print(f"  ✓ {OUTPUT_KML}")
        print(f"  ✓ {OUTPUT_COORDENADAS}")
        print(f"  ✓ {OUTPUT_WKT}")
        print(f"  ✓ {OUTPUT_WKT_POINT}")
        print(f"  ✓ {OUTPUT_SQL}")

        print(f"\nTotal de coordenadas: {len(coordenadas_scp)}")
        print(f"Geometría válida: {poligono.is_valid}")
        print(f"Tipo de geometría: {poligono.geom_type}")