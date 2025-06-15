#Código portable en Python (Cliente UDP)
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.sendto("Hola, servidor UDP".encode(), ("127.0.0.1", 8080))
respuesta, _ = cliente.recvfrom(1024)
print("Respuesta del servidor:", respuesta.decode())
cliente.close()

#Crear socket UDP
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Enviar datagrama
cliente.sendto("Hola, servidor UDP".encode(), ("127.0.0.1", 8080))
#Esperar respuesta
respuesta, _ = cliente.recvfrom(1024)
#Leer respuesta
print("Respuesta del servidor:", respuesta.decode())
#Cerrar socket
cliente.close()





