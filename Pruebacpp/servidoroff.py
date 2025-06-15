import socket
import os

IP = "127.0.0.1"
PUERTO = 9090
BUFFER_SIZE = 1024

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP, PUERTO))
servidor.listen(1)

print(f"Servidor TCP escuchando en {IP}:{PUERTO}")

conn, addr = servidor.accept()
print(f"Conexión establecida con {addr}")

mensaje = conn.recv(BUFFER_SIZE).decode()
print(f"Mensaje recibido: {mensaje}")

if mensaje.upper() == "APAGAR":
    conn.send("Apagando el sistema...".encode())
    print("Ejecutando apagado del sistema...")
    os.system("shutdown /s /t 1")  # Windows
    # os.system("sudo shutdown now")  # Linux (requiere sudo)
else:
    conn.send("Comando recibido correctamente.".encode())

conn.close()
servidor.close()
