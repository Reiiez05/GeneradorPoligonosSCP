# ==========================================================
# GENERADOR DE POLÍGONOS SCP
# Configuración General
# ==========================================================


# ==========================================================
# ENTRADA
# ==========================================================

INPUT_KML = "input/REGION I XICOTEPEC.kml"


# ==========================================================
# SALIDAS
# ==========================================================

OUTPUT_KML = "output/buffer20m.kml"

OUTPUT_COORDENADAS = "output/coordenadas_scp.txt"

OUTPUT_WKT = "output/geocerca.wkt"

OUTPUT_WKT_POINT = "output/centro.wkt"

OUTPUT_SQL = "output/insertar_zona.sql"


# ==========================================================
# PROCESAMIENTO GEOMÉTRICO
# ==========================================================

# Distancia del buffer en metros
BUFFER_METROS = 50

# Reservado para versiones futuras
SIMPLIFICACION = 5


# ==========================================================
# CONFIGURACIÓN SCP
# ==========================================================

SRID = 4326

USUARIO_ID = 1

STATUS_ZONA = 1

COLOR_ZONA = "rgb(0,0,0)"


# ==========================================================
# INFORMACIÓN DE LA ZONA
# ==========================================================

NOMBRE_ZONA = "PRUEBA"

DESCRIPCION_ZONA = "Generado desde Python"