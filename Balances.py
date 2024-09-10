import hashlib
import hmac
import time
import requests
from dotenv import load_dotenv
import os

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

# Realizar la solicitud
headers = {
    'X-Auth-Apikey': api_key,
    'X-Auth-Nonce': nonce,
    'X-Auth-Signature': signature
}

# Realizar la solicitud
response = requests.get('https://app.aion.com.mx/api/v2/peatio/account/balances', headers=headers)

# Imprimir la respuesta
print(response.status_code)
print(response.json())
