import socket

def pedir_opcion(cliente, opciones):
    while True:
        try:
            cliente.sendall("Selecciona una opción:\n" + "\n".join(opciones).encode())
            opcion = cliente.recv(1024).decode()
            if opcion in [opcion.split('-')[0] for opcion in opciones]:
                return opcion
            else:
                cliente.sendall("Opción inválida, por favor intenta de nuevo.".encode())
        except Exception as e:
            print(f"Error al recibir la opción: {e}")
            return None

def main():
    port = 12345
    host = "localhost"

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(2)
    print("Esperando la conexión...")

    conn1, addr1 = serverSocket.accept()
    print(f"Cliente 1 conectado desde {addr1}")

    conn2, addr2 = serverSocket.accept()
    print(f"Cliente 2 conectado desde {addr2}")

    
    opcColores = ["1- Rojo", "2- Verde", "3- Azul"]
    opcFruta = ["1- Manzana", "2- Frutilla", "3- Pera"]
    opcMarca = ["1- Nike", "2- Adidas", "3- Puma"]

    
    score_cliente1 = 0
    score_cliente2 = 0

    
    colorCliente1 = pedir_opcion(conn1, opcColores)
    frutaCliente1 = pedir_opcion(conn1, opcFruta)
    marcaCliente1 = pedir_opcion(conn1, opcMarca)

    colorCliente2 = pedir_opcion(conn2, opcColores)
    frutaCliente2 = pedir_opcion(conn2, opcFruta)
    marcaCliente2 = pedir_opcion(conn2, opcMarca)

 
    colorAdivinador = pedir_opcion(conn2, opcColores)
    frutaAdivinador = pedir_opcion(conn2, opcFruta)
    marcaAdivinador = pedir_opcion(conn2, opcMarca)

   
    if colorCliente1 == colorAdivinador:
        print(f"El Cliente 2 adivinó el color correctamente ({colorCliente1})")
        score_cliente2 += 1
    else:
        print("El Cliente 2 no adivinó el color")

    if frutaCliente1 == frutaAdivinador:
        print(f"El Cliente 2 adivinó la fruta correctamente ({frutaCliente1})")
        score_cliente2 += 1
    else:
        print("El Cliente 2 no adivinó la fruta")

    if marcaCliente1 == marcaAdivinador:
        print(f"El Cliente 2 adivinó la marca correctamente ({marcaCliente1})")
        score_cliente2 += 1
    else:
        print("El Cliente 2 no adivinó la marca")

    
    print(f"\nPuntaje final:")
    print(f"Cliente 1: {score_cliente1}")
    print(f"Cliente 2: {score_cliente2}")

   
    conn1.close()
    conn2.close()
    serverSocket.close()

if __name__ == "__main__":
    main()
