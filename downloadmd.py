import csv
import requests
import time
import os

# Ruta al archivo CSV
archivo_csv = '/home/edgarblas/Desktop/mdschido.csv'
carpeta_descargas = '/home/edgarblas/Desktop/mdsDownload/'
resultados = []

with open(archivo_csv, 'r', newline='') as archivo:
    lector_csv = csv.reader(archivo)
    print(lector_csv)
    contador = 0
    # Itera sobre cada fila del archivo CSV
    for fila in lector_csv:
        print(fila)
        print(fila[1])

        # Convertir la fila a un objeto JSON
        fila_json = {
            "id": fila[0],
            "upc": fila[1],
            "titulo": fila[2],
            "cve_soft": fila[3],
            "edicion": fila[4],
            "cve_carta": fila[5],
            "res": fila[6],
            "mod": fila[7],
            "datum": fila[8],
            "url_descarga": fila[9],
            "archivo": fila[10]
        }

        # Agregar el objeto JSON a la lista de resultados
        resultados.append(fila_json)
    print(resultados)

    # Iterar sobre cada objeto de descarga
    for objeto in resultados:
        print('objeto', objeto)
        # Obtener el enlace de descarga del objeto actual
        url_descarga = objeto['url_descarga']  # Aquí se obtiene la URL de descarga del objeto actual
        print(url_descarga)

        # Incrementar el contador en cada iteración
        contador += 1

        # Realizar la solicitud GET para descargar el archivo solo a partir de la vuelta 35
        if contador >= 35:
            response = requests.get(url_descarga)  # Aquí se utiliza la variable url_descarga

            # Verificar si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                print(f"Descargando {objeto['archivo']}...")

                # Obtener el nombre del archivo descargado
                nombre_archivo = objeto['cve_carta'] + ".zip"

                # Establecer la ruta completa de descarga
                ruta_descarga = os.path.join(carpeta_descargas, nombre_archivo)

                # Guardar el archivo descargado (en este caso, no se guarda, solo se simula)
                # Aquí podrías agregar el código para guardar el archivo en tu sistema de archivos
                with open(ruta_descarga, 'wb') as archivo_descargado:
                    archivo_descargado.write(response.content)

                print(f"{objeto['archivo']} descargado exitosamente.")

                # Introducir un retraso de 10 segundos entre cada descarga
                time.sleep(5)
            else:
                print(f"Error al descargar {objeto['archivo']}: Código de estado {response.status_code}")
