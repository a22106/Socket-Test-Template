import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8505

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    # Bind the socket to the server host and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    # Listen for data from the client
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print('Received from client:', repr(data))

        # Send data back to the client
        server_socket.sendto(b'Hello from the server!', client_address)
