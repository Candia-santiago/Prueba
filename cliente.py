import socket

host = "localhost"
port= 12345

clienteSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, port))
print ("cliente conectado al server...")

colorCliente = input ("Seleccione un color para jugar [1- Rojo 2-Verde, 3- Azul]: ")
clienteSocket.send(colorCliente.encode())

frutaCliente = input ("seleccione una fruta para jugar [1-Manzana 2-frutilla 3-Pera]: ")
clienteSocket.send(frutaCliente.encode())

marcaCliente = input("seleccione una marca para jugar [1-Nike 2-Adidas 3-Puma]: ")
clienteSocket.send(marcaCliente.encode())

clienteSocket.close()