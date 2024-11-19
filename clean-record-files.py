import pandas as pd
import os

# Ruta al archivo CSV individual
archivo_csv = 'AA0009_Energy.csv'

# Verifica si el archivo existe
if os.path.isfile(archivo_csv):
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv)

    # Filtrar los registros donde tDays <= 60
    df_filtrado = df[df['tDays'] <= 60]

    # Procesar los datos como lo necesites (crear nuevas columnas, etc.)
    df_filtrado['id'] = df_filtrado.index  # O asigna un valor específico
    df_filtrado['nest'] = 'TS-NA0009'  # Esto depende de cómo obtengas el ID del nido
    df_filtrado['samplingDateTime'] = pd.Timestamp.now()  # Fecha y hora actual
    df_filtrado['Temp'] = df_filtrado['Temp'] / 25.6
    df_filtrado['humidityPercentage'] = 0
    df_filtrado['Energy'] = df_filtrado['Energy']
    df_filtrado['X'] = df_filtrado['X']
    df_filtrado['Y'] = df_filtrado['Y']
    df_filtrado['Z'] = df_filtrado['Z']
    df_filtrado['isTesting'] = False  # Ajusta según la lógica de tu programa
    df_filtrado['recordNumber'] = df_filtrado.index + 1
    df_filtrado['day'] = df_filtrado['tDays']

    # Seleccionar solo las columnas necesarias
    columnas_necesarias = [
        'id', 'nest', 'samplingDateTime', 'Temp',
        'humidityPercentage', 'Energy', 'X', 'Y', 'Z', 
        'isTesting', 'recordNumber', 'day'
    ]
    
    # Guardar el DataFrame filtrado con solo las columnas necesarias
    df_filtrado[columnas_necesarias].to_csv('TS-NA0009-AA0009.csv', index=False)

    print("El archivo se ha procesado y guardado como 'TS-NA0003-AA0003.csv'.")
else:
    print(f"El archivo '{archivo_csv}' no existe.")
