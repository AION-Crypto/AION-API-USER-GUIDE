import requests

# URL de la API para conseguir el timestamp
url = "https://app.aion.com.mx/api/v2/peatio/public/timestamp"

# Realizar la solicitud
response = requests.request("GET", url)

# Imprimir la respuesta
r_json = response.json()
print(r_json)
