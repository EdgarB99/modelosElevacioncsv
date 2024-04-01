import csv
import requests
import json

# URL de la solicitud POST
url = 'https://www.inegi.org.mx/app/geo2/elevacionesmex/getF10KDescarga.do'

# Encabezados de la solicitud
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'es-419,es;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=C48C9F14A0C36E2EB6CFEBAF42B09984; _ga_SBVWFG0RDV=GS1.1.1711987982.7.1.1711988004.0.0.0; _ga=GA1.3.1132650150.1711653752; BIGipServerLB_app_geo2=1745000714.38175.0000; BIGipServerLB_NuevoPortal=1208129802.20480.0000; _gid=GA1.3.1249357084.1711987983; _gat=1; BIGipServerLB_contenidos2=1191352586.37407.0000',
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

# Datos que se enviarán en la solicitud
data = {
    'res': '5',
    'mod': 'T',
    'cve': 'E14A23E1'
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
# Mostrar el resultado modificado
print(json.dumps(data, indent=4))


