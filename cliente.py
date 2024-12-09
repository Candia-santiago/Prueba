import socket

# Configuración básica del cliente
host = "localhost"
port = 12345

# Crear el socket del cliente
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))

try:
    while True:
        # Recibir mensaje del servidor
        mensaje = clientSocket.recv(1024).decode()
        if not mensaje:
            break
        print(mensaje)  # Mostrar el mensaje recibido
        
        # Si el servidor solicita una respuesta, enviarla
        if "Selecciona" in mensaje or "Adivina" in mensaje:
            respuesta = input("Tu elección: ")
            clientSocket.send(respuesta.encode())
except:
    print("Conexión finalizada.")
finally:
    clientSocket.close()
