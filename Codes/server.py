import socket,threading

clients=[]

def handle_client(client_socket):
    while True:
        try:
            data=client_socket.recv(1024)
            if not data:
                break
            broadcast(data,client_socket)
        except:
            break
    
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message,sender_socket):
    for client in clients :
        if client !=sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                client.remove(client)
def start_server():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',24131))
    server.listen()
    print('Server is started listening:')

    while True:
        clients_socket,addr=server.accept()
        print('New Connection is happening: ',clients_socket,addr)
        clients.append(clients_socket)
        thread = threading.Thread(target=handle_client,args=(clients_socket,))
        thread.start()

if __name__=='__main__':
    start_server()
