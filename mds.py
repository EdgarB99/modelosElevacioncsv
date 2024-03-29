import csv
import requests
import json

resultados = []
# Ruta al archivo CSV
archivo_csv = '/home/edgarblas/Desktop/mds.csv'
# URL de la solicitud POST
url = 'https://www.inegi.org.mx/app/geo2/elevacionesmex/getF10KDescarga.do'

# Encabezados de la solicitud
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'es-419,es;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=7948273F519F8C795D5893853B821436; _ga_SBVWFG0RDV=GS1.1.1711729944.5.1.1711729973.0.0.0; _ga=GA1.3.1132650150.1711653752; _gid=GA1.3.1925182207.1711653755; BIGipServerLB_app_geo2=1745000714.37919.0000; BIGipServerLB_NuevoPortal=1208129802.20480.0000; _gat=1; BIGipServerLB_contenidos2=1191352586.37407.0000',
    'Origin': 'https://www.inegi.org.mx',
    'Referer': 'https://www.inegi.org.mx/app/geo2/elevacionesmex/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}


# Abre el archivo CSV en modo lectura
with open(archivo_csv, 'r', newline='') as archivo:
    lector_csv = csv.reader(archivo)
    print(lector_csv)
    contador = 0
    # Itera sobre cada fila del archivo CSV
    for fila in lector_csv:
        print(fila)
        print(fila[1])
        # Datos que se enviarán en la solicitud
        data = {
            'res': '5',
            'mod': 'T',
            'cve': fila[2]
        }
        # Realiza la solicitud POST utilizando requests
        response = requests.post(url, data=data, headers=headers)

        # Muestra la respuesta recibida
        print(response.text)

        # Manejo de errores
        if response.status_code != 200:
            print('Error al hacer la solicitud:', response.status_code)

        # Response text recibido
        response_text = response.text

        # Parsear el JSON
        data = json.loads(response_text)

        # Iterar sobre cada elemento
        if len(data) == 2:
            # Verificar si "_as.zip" está en el archivo
            if '_as.zip' in data[1]['archivo']:
                data[1]['url_descarga'] += '_as.zip'
            # Si no, verificar "_gr.zip"
            elif '_gr.zip' in data[1]['archivo']:
                data[1]['url_descarga'] += '_gr.zip'
            # Si no, agregar "_b.zip"
            else:
                data[1]['url_descarga'] += '_b.zip'

            resultados.append(data[1])
            # Mostrar el resultado modificado
            print(json.dumps(data, indent=4))
        # Iterar sobre cada elemento
        elif len(data) == 3:
            # Verificar si "_as.zip" está en el archivo
            if '_as.zip' in data[2]['archivo']:
                data[2]['url_descarga'] += '_as.zip'
            # Si no, verificar "_gr.zip"
            elif '_gr.zip' in data[2]['archivo']:
                data[2]['url_descarga'] += '_gr.zip'
            # Si no, agregar "_b.zip"
            else:
                data[2]['url_descarga'] += '_b.zip'

            resultados.append(data[2])
            # Mostrar el resultado modificado
            print(json.dumps(data, indent=4))
        else:
            for item in data:
                # Verificar si "_as.zip" está en el archivo
                if '_as.zip' in item['archivo']:
                    item['url_descarga'] += '_as.zip'
                # Si no, verificar "_gr.zip"
                elif '_gr.zip' in item['archivo']:
                    item['url_descarga'] += '_gr.zip'
                # Si no, agregar "_b.zip"
                else:
                    item['url_descarga'] += '_b.zip'

                resultados.append(item)
            contador += 1
            # Mostrar el resultado modificado
            print(json.dumps(data, indent=4))

print('resultados',resultados)

# Guardar los resultados en un archivo CSV

# Obtener las claves del primer diccionario para escribir los encabezados del CSV
headers = resultados[0].keys()

# Especificar el nombre del archivo CSV
csv_filename = '/home/edgarblas/Desktop/mdt.csv'

# Escribir los datos en el archivo CSV
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)

    # Escribir los encabezados
    writer.writeheader()

    # Escribir cada fila de datos
    for row in resultados:
        writer.writerow(row)

print(f"Se ha creado el archivo CSV '{csv_filename}' con éxito.")
