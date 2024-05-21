import socket

def client():
    # Obtener el hostname (ya que tanto cliente como server correrán en tu máquina)
    host = socket.gethostname()

    # Definir el número de puerto para comunicarse con el servidor
    port = 12345
    # TO DO
    
    # Crear un objeto socket
    client_socket = socket.socket()

    # Conectar al servidor especificando el hostname y el puerto
    client_socket.connect((host, port))

    # Pedir al usuario un input
    message = input("Ingresá un mensaje (Poner 'chau' para salir): ")
    while message.lower().strip() != "bye":
        # Enviar el mensaje al server (usar message.encode())
        client_socket.send(message.encode())
        # TO DO

        # Recibir una respuesta del servidor
        data = client_socket.recv(1024).decode()

        # Mostrar el mensaje recibido del servidor
        print("Received from server: " + data)
        
        # Pedir un nuevo mensaje
        # TO DO
        message = input("mandame un nuevo mensaje: ")
    # Cerrar la conexión
    client_socket.close()
    # TO DO


if __name__ == "__main__":
    client()
