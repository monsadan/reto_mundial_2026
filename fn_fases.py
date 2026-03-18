import pandas as pd

def dieciseisavos(lista_paises, estructura_partidos, nombre_archivo="Dieciseisavos_2026.xlsx"):
    """
    lista_paises: List of dicts [{'pais': 'Mexico', 'pos': '1º', 'grupo': 'A'}]
    estructura_partidos: The raw data you provided
    """
    
    # 1. Create a lookup dictionary: "1º Grupo A" -> "Mexico"
    mapeo_paises = {f"{p['pos']} Grupo {p['grupo']}": p['pais'] for p in lista_paises}
    
    # 2. Process the rows
    datos_finales = []
    for fila in estructura_partidos:
        # Extract original references
        ref_local = fila[2]
        ref_visitante = fila[3]
        
        # Replace with country name if found, otherwise keep the placeholder
        pais_local = mapeo_paises.get(ref_local, ref_local)
        pais_visitante = mapeo_paises.get(ref_visitante, ref_visitante)
        
        datos_finales.append({
            "Fase": fila[0],
            "Partido #": fila[1],
            "Local": pais_local,
            "Visitante": pais_visitante,
            "Fecha": fila[4]
        })
    
    # 3. Create DataFrame and export to Excel
    df = pd.DataFrame(datos_finales)
    df.to_excel(nombre_archivo, index=False)
    print(f"✅ Excel generated successfully: {nombre_archivo}")


def octavos(diccionario_ganadores, nombre_archivo="octavos_final_2026.xlsx"):
    """
    Toma un diccionario {id_partido: 'País'} y genera un archivo Excel 
    con el formato de la tabla de octavos.
    """
    
    # Esquema oficial de los cruces de octavos
    datos_base = [
        ["Octavos", 89, 74, 77, "4 de julio de 2026"],
        ["Octavos", 90, 73, 75, "4 de julio de 2026"],
        ["Octavos", 91, 76, 78, "5 de julio de 2026"],
        ["Octavos", 92, 79, 80, "5 de julio de 2026"],
        ["Octavos", 93, 81, 82, "6 de julio de 2026"],
        ["Octavos", 94, 83, 84, "6 de julio de 2026"],
        ["Octavos", 95, 85, 86, "7 de julio de 2026"],
        ["Octavos", 96, 87, 88, "7 de julio de 2026"],
    ]

    tabla_final = []

    for fila in datos_base:
        fase, id_oct, id_p1, id_p2, fecha = fila
        
        # Buscamos el nombre del país en el diccionario, si no está, ponemos el ID genérico
        pais_1 = diccionario_ganadores.get(id_p1, f"Ganador Partido {id_p1}")
        pais_2 = diccionario_ganadores.get(id_p2, f"Ganador Partido {id_p2}")
        
        tabla_final.append([fase, id_oct, pais_1, pais_2, fecha])

    # Crear el DataFrame de Pandas
    df = pd.DataFrame(tabla_final, columns=["Fase", "ID Octavos", "País 1", "País 2", "Fecha"])

    # Exportar a Excel
    df.to_excel(nombre_archivo, index=False)
    print(f"✅ Archivo '{nombre_archivo}' generado con éxito.")


def cuartos(paises_ganadores):
    """
    paises_ganadores: Diccionario con el número de partido previo y el país.
    Ejemplo: {89: "Argentina", 90: "Francia", ...}
    """
    
    # Estructura base de la tabla
    datos = [
        ["Cuartos", 97, f"Ganador {paises_ganadores.get(89, 'Partido 89')}", f"Ganador {paises_ganadores.get(90, 'Partido 90')}", "9 de julio de 2026"],
        ["Cuartos", 98, f"Ganador {paises_ganadores.get(93, 'Partido 93')}", f"Ganador {paises_ganadores.get(94, 'Partido 94')}", "10 de julio de 2026"],
        ["Cuartos", 99, f"Ganador {paises_ganadores.get(91, 'Partido 91')}", f"Ganador {paises_ganadores.get(92, 'Partido 92')}", "11 de julio de 2026"],
        ["Cuartos", 100, f"Ganador {paises_ganadores.get(95, 'Partido 95')}", f"Ganador {paises_ganadores.get(96, 'Partido 96')}", "11 de julio de 2026"],
    ]
    
    # Crear el DataFrame
    df = pd.DataFrame(datos, columns=["Fase", "Partido #", "Equipo 1", "Equipo 2", "Fecha"])
    
    # Exportar a Excel
    nombre_archivo = "calendario_cuartos.xlsx"
    df.to_excel(nombre_archivo, index=False)
    
    return f"Archivo '{nombre_archivo}' generado con éxito."

def semis(datos_partidos, nombre_archivo="Semifinales_2026.xlsx"):
    """
    Recibe un diccionario con {numero_partido: "País"} 
    Ejemplo: {97: "España", 98: "Brasil", 99: "Francia", 100: "Argentina"}
    """
    
    # Estructura base de la tabla según tu solicitud
    tabla = [
        ["Semifinal", 101, datos_partidos.get(97), datos_partidos.get(98), "14 de julio de 2026"],
        ["Semifinal", 102, datos_partidos.get(99), datos_partidos.get(100), "15 de julio de 2026"]
    ]
    
    columnas = ["Fase", "ID Partido", "Ganador Partido A", "Ganador Partido B", "Fecha"]
    df = pd.DataFrame(tabla, columns=columnas)
    
    df.to_excel(nombre_archivo, index=False)
    print(f"Archivo '{nombre_archivo}' creado con éxito.")

def finalistas(p101_equipo_a, p101_equipo_b, ganador_101, 
                          p102_equipo_a, p102_equipo_b, ganador_102):
    
    # Lógica para encontrar a los perdedores
    perdedor_101 = p101_equipo_b if ganador_101 == p101_equipo_a else p101_equipo_a
    perdedor_102 = p102_equipo_b if ganador_102 == p102_equipo_a else p102_equipo_a
    
    # Estructura de los datos según tu requerimiento
    datos = [
        {
            "Partido": "Tercer Puesto",
            "ID": 103,
            "Equipo 1": perdedor_101,
            "Equipo 2": perdedor_102,
            "Fecha": "18 de julio de 2026"
        },
        {
            "Partido": "Final",
            "ID": 104,
            "Equipo 1": ganador_101,
            "Equipo 2": ganador_102,
            "Fecha": "19 de julio de 2026"
        }
    ]
    
    # Crear DataFrame y exportar
    df = pd.DataFrame(datos)
    nombre_archivo = "calendario_fase_final.xlsx"
    df.to_excel(nombre_archivo, index=False)
    
    return f"¡Archivo '{nombre_archivo}' generado con éxito!"
