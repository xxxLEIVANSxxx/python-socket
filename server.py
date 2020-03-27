import socket

port = input("PORTA(ex:9000) >> ")
print("")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = sock.bind(('localhost', int(port)))

sock.listen(1)

aux = True;

while aux:
    mensagem = input("MSG >> ")
    tamanho_da_mensagem = len(mensagem)

    connection, address_client = sock.accept()    
    
    connection.sendall(str(tamanho_da_mensagem).zfill(4).encode())
    
    connection.sendall(mensagem.encode())

    if mensagem == "see ya":
        aux = False
    else:
        expected_data_size = ''
        while(expected_data_size == ''):
            expected_data_size += connection.recv(4).decode()
        expected_data_size = int(expected_data_size)

        received_data = ''
        while len(received_data) < expected_data_size:
            received_data += connection.recv(4).decode()
        print("Resposta do cliente: " + received_data)
        
        if received_data == "see ya":
            aux = False;
    connection.close()

print("Finalizando...");
sock.close()
