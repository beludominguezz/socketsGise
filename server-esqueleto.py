import socket

def server():
    # Obtener el hostname
    host = socket.gethostname()

    # Especificar el puerto para escuchar
    port = 12345
    # TO DO

    # Crear un objeto socket
    s = socket.socket()

    # Bindear el socket al host y al puerto
    s.bind((host, port))

    # Escuchar conexiones ingresantes
    s.listen(1)
    # TO DO

    # Aceptar conexiones entrantes
    c, address = s.accept()
    print(f"Connected to: {address}")

    newMsg = True
    while newMsg:
        # Recibir datos del cliente (hasta 1024 bytes)
        data = c.recv(1024).decode()

        # setear en newMsg si hay data nueva (si no, rompe el ciclo)
        newMsg = data
        print(f"Recibido de cliente: {data}")

        # Obtener el input de usuario y enviar al cliente (usar response.encode())
        response = input("Enter response to send to client: ")
        c.send(response.encode())
        # TO DO

    # Cerrar la conexión con el cliente
    c.close()
    # TO DO


if __name__ == "__main__":
    # Start the server
    server()
