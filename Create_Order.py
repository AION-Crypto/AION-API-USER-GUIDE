import hashlib
import hmac
import time
import requests
import json
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Tus credenciales de API
api_key = os.getenv('AION_API_KEY')
api_secret = os.getenv('AION_API_SECRET')

# Generar nonce
nonce = str(int(time.time() * 1000))

# Crear el mensaje para la firma
message = nonce + api_key

# Calcular la firma
signature = hmac.new(api_secret.encode(), message.encode(), hashlib.sha256).hexdigest()

# Crear las cabezeras
headers = {
    'X-Auth-Apikey': api_key,
    'X-Auth-Nonce': nonce,
    'X-Auth-Signature': signature
}

# Crear el la data que se enviara a la API
payload = json.dumps({
    'market': 'usdtmxn',
    'side': 'buy',
    'volume': 10.0,
    'price': 19.0
})

# Realizar la solicitud
response = requests.post('https://app.aion.com.mx/api/v2/peatio/market/orders', headers=headers, data=payload)

#Imprimir la respuesta
print(response.status_code)
print(response.json())
