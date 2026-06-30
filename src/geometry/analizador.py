from shapely.geometry import Polygon, MultiPolygon


def analizar_geometria(geometria):

    print("\n========== ANÁLISIS ==========")

    print(f"Tipo: {geometria.geom_type}")

    print(f"Válida: {geometria.is_valid}")

    print(f"Área: {geometria.area:,.2f} m²")

    if isinstance(geometria, Polygon):

        print("\n--- Polygon ---")

        print(f"Huecos: {len(geometria.interiors)}")

        print(f"Vértices exteriores: {len(geometria.exterior.coords)}")

    elif isinstance(geometria, MultiPolygon):

        print("\n--- MultiPolygon ---")

        print(f"Cantidad de polígonos: {len(geometria.geoms)}")

        for i, pol in enumerate(geometria.geoms):

            print(
                f"Polígono {i+1}: "
                f"Área={pol.area:,.2f} "
                f"Huecos={len(pol.interiors)} "
                f"Vértices={len(pol.exterior.coords)}"
            )

    print("==============================\n")