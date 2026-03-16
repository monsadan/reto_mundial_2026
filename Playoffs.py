import pandas as pd

def elegir_ganador(opciones, titulo_partido):
    print(f"\n{titulo_partido}")
    for i, equipo in enumerate(opciones, 1):
        print(f"({i}) {equipo}")
    
    while True:
        eleccion = input("Selecciona el ganador (número): ")
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
            return opciones[int(eleccion)-1]
        print("Entrada no válida. Intenta de nuevo.")

def simular_clasificacion_2026():
    print("=== SIMULADOR DE REPESCA MUNDIAL 2026 ===")
    resultados = []

    # 1. PLAYOFFS INTERCONTINENTALES (FIFA)
    # Según sorteo: Ruta 1 va al Grupo K, Ruta 2 va al Grupo I
    fifa_paths = {
        "FIFA Ruta 1": {"semi": ["Nueva Caledonia", "Jamaica"], "espera": "RD Congo", "grupo": "Grupo K"},
        "FIFA Ruta 2": {"semi": ["Bolivia", "Surinam"], "espera": "Irak", "grupo": "Grupo I"}
    }
    
    print("\n--- FASE INTERCONTINENTAL ---")
    for nombre, datos in fifa_paths.items():
        ganador_semi = elegir_ganador(datos["semi"], f"Semifinal {nombre}")
        ganador_final = elegir_ganador([ganador_semi, datos["espera"]], f"FINAL {nombre}")
        resultados.append({"Torneo": "FIFA Intercontinental", "Ruta": nombre, "Clasificado": ganador_final, "Grupo Mundial": datos["grupo"]})

    # 2. PLAYOFFS UEFA
    # Asignaciones oficiales de grupos para ganadores de ruta
    uefa_paths = {
        "UEFA Ruta A": {"semis": [("Italia", "Irlanda del Norte"), ("Gales", "Bosnia y Herz.")], "grupo": "Grupo B"},
        "UEFA Ruta B": {"semis": [("Ucrania", "Suecia"), ("Polonia", "Albania")], "grupo": "Grupo F"},
        "UEFA Ruta C": {"semis": [("Turquía", "Rumanía"), ("Eslovaquia", "Kosovo")], "grupo": "Grupo D"},
        "UEFA Ruta D": {"semis": [("Dinamarca", "Macedonia del Norte"), ("Chequia", "Rep. de Irlanda")], "grupo": "Grupo A"}
    }

    print("\n--- FASE UEFA (EUROPA) ---")
    for ruta, datos in uefa_paths.items():
        print(f"\n>> {ruta}")
        g1 = elegir_ganador(list(datos["semis"][0]), "Semifinal 1")
        g2 = elegir_ganador(list(datos["semis"][1]), "Semifinal 2")
        ganador_final = elegir_ganador([g1, g2], f"FINAL {ruta}")
        resultados.append({"Torneo": "UEFA Europa", "Ruta": ruta, "Clasificado": ganador_final, "Grupo Mundial": datos["grupo"]})

    # Crear DataFrame y guardar en Excel
    df = pd.DataFrame(resultados)
    nombre_archivo = "clasificados_mundial_2026.xlsx"
    df.to_excel(nombre_archivo, index=False)

    print("\n" + "="*50)
    print(f"¡SIMULACIÓN COMPLETADA!")
    print(f"Se ha generado el archivo: {nombre_archivo}")
    print("="*50)
    print(df[["Clasificado", "Grupo Mundial"]].to_string(index=False))

if __name__ == "__main__":
    simular_clasificacion_2026()

