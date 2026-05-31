import socket
import os
from datetime import datetime

HOST = "postgres"
PORT = 5432

print("=" * 50)
print("Validación PostgreSQL")
print("=" * 50)
print(f"Fecha: {datetime.now()}")

try:
    sock = socket.create_connection((HOST, PORT), timeout=5)
    sock.close()

    print(f"Estado: OK")
    print(f"Host: {HOST}")
    print(f"Puerto: {PORT}")
    print("Conectividad correcta")

except Exception as e:
    print(f"Estado: ERROR")
    print(f"Detalle: {e}")