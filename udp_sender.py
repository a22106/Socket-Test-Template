import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8505

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Send data to the server
    client_socket.sendall(b'Hello from the client!')

    # Receive data from the server
    data = client_socket.recv(1024)
    print('Received from the server:', repr(data))