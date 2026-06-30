# SCP GeoTools

## Objetivo

Convertir rutas KML (LineString) en polígonos compatibles con SCP.

## Estado

Versión actual: v0.3

## Flujo

KML
↓
Lectura
↓
UTM
↓
Buffer
↓
Limpieza
↓
Contorno
↓
Simplificación
↓
Exportación