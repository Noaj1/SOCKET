import socket

IP_SERVIDOR = "127.0.0.1"
PUERTO_SERVIDOR = 9090

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP_SERVIDOR, PUERTO_SERVIDOR))

# Aquí envías el comando al servidor
cliente.send("APAGAR".encode())

respuesta = cliente.recv(1024).decode()
print("Respuesta del servidor:", respuesta)

cliente.close()
