import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8505 # Port for listening

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Set the socket to be reusable. This prevents the "Address already in use" error
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    print('Server is starting up...')

    # Listen for connections
    server_socket.listen(1) # Only one connection is allowed. Set it to 0 for unlimited connections
    print('Server is listening on {}:{}'.format(SERVER_HOST, SERVER_PORT))
    print('Waiting for a connection...')

    # Accept a connection
    client_socket, addr = server_socket.accept() 
    
    with client_socket:
        print('Connected by', addr)

        # Receive data from the client
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print('Received from the client:', repr(data))

            # Send data to the client
            # client_socket.sendall(b'Hello from the server!')
