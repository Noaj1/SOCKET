import socket

# Crear socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Esperando conexión...")

conn, addr = server_socket.accept()
print(f"Conectado por {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Recibido:", data.decode())
    conn.sendall(b"Hola cliente")

conn.close()
server_socket.close()


