# Historial

## v0.3

- Lectura de KML
- Conversión automática a UTM
- Buffer
- Limpieza básica
- Exportación KML

## v1.1 - Sprint 1

### Refactorización de arquitectura

- Se creó el módulo `core`.
- Se implementó `GeneradorPoligonosEngine`.
- `main.py` quedó como punto de entrada.
- Se reorganizó `config.py`.
- Se centralizaron las rutas de salida.
- Se refactorizó `engine.py` en métodos privados.
- Se mejoró la separación de responsabilidades.
- No hubo cambios en el motor geométrico.
- Compatibilidad total con la versión 1.0.