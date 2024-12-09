import socket

host = "localhost"
port = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(2)
print("Esperando la conexión de los clientes...")

conn1, addr1 = serverSocket.accept()
print(f"Cliente 1 conectado desde {addr1}")
conn1.send("Bienvenido Cliente 1! Eres el seleccionador.\n".encode())

conn2, addr2 = serverSocket.accept()
print(f"Cliente 2 conectado desde {addr2}")
conn2.send("Bienvenido Cliente 2! Eres el adivinador.\n".encode())

opcColores = ["1- Rojo", "2- Verde", "3- Azul"]
opcFrutas = ["1- Manzana", "2- Frutilla", "3- Pera"]
opcMarcas = ["1- Nike", "2- Adidas", "3- Puma"]

def pedir_opcion(conn, opciones):
    conn.send(f"Selecciona una opc:\n{chr(10).join(opciones)}\n".encode())
    return conn.recv(1024).decode().strip()

score_cliente2 = 0

conn1.send("Selecciona tus opciones:\n".encode())
color1 = pedir_opcion(conn1, opcColores)
fruta1 = pedir_opcion(conn1, opcFrutas)
marca1 = pedir_opcion(conn1, opcMarcas)


conn2.send("Intenta adivinar las opciones del Cliente 1:\n".encode())
adiv_color2 = pedir_opcion(conn2, opcColores)
if adiv_color2 == color1:
    score_cliente2 += 1
    conn2.send("Adivinaste el color correctamente!\n".encode())
else:
    conn2.send("No adivinaste el color.\n".encode())

adiv_fruta2 = pedir_opcion(conn2, opcFrutas)
if adiv_fruta2 == fruta1:
    score_cliente2 += 1
    conn2.send("Adivinaste la fruta correctamente!\n".encode())
else:
    conn2.send("No adivinaste la fruta.\n".encode())

adiv_marca2 = pedir_opcion(conn2, opcMarcas)
if adiv_marca2 == marca1:
    score_cliente2 += 1
    conn2.send("Adivinaste la marca correctamente!\n".encode())
else:
    conn2.send("No adivinaste la marca.\n".encode())

conn2.send(f"Tu puntuacion final es: {score_cliente2}\n".encode())
print(f"Puntuacion final del Cliente 2: {score_cliente2}")

conn1.close()
conn2.close()
serverSocket.close()
