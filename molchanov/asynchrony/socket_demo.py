import socket

# server:
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 55111))
server_socket.listen()


while True:
    print('\nBefore .accept() method\nWaiting for an incoming connection from a client..')
    client_socket, addr = server_socket.accept()  # the point for an incoming connection
    # There is an incoming connection:
    print(f'\nGet connection for a Client from: {addr}')
    # waiting for client data:

    while True:
        print('\nBefore .recv() method')
        request = client_socket.recv(4096)  # buffer size 4k
        if not request:
            break
        else:
            response = 'Hello user!\n'.encode()
            client_socket.send(response)
    
    print('\n! ! ! The server has left the inner while loop ! ! !\n')
    client_socket.close()
