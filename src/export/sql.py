from config import *


def generar_insert_sql(
    nombre,
    descripcion,
    wkt_poligono,
    wkt_punto,
    zona_padre=None
):
    """
    Genera el INSERT de una zona
    compatible con SCP.
    """

    valor_zona = "NULL" if zona_padre is None else str(zona_padre)

    sql = f"""
INSERT INTO dbo.zonas
(
    Zn_Nombre,
    Zn_Descripcion,
    Zn_FechaRegistro,
    Zn_FechaModificacion,
    Zn_UsuarioRegistro,
    Zn_UsuarioModifico,
    Zn_Status,
    Zn_Geocerca,
    Zn_GeopuntoCentro,
    Zn_Zonas,
    Zn_Unificador
)
VALUES
(
    '{nombre}',
    '{descripcion}',
    GETDATE(),
    GETDATE(),
    {USUARIO_ID},
    {USUARIO_ID},
    {STATUS_ZONA},

    geography::STGeomFromText(
'{wkt_poligono}',
{SRID}
),

    geography::STGeomFromText(
'{wkt_punto}',
{SRID}
),

    {valor_zona},

    '{COLOR_ZONA}'
);
"""

    return sql