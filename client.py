import socket

port = input("PORTA(ex:9000) >> ")
print("")

aux = True
while aux:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', int(port)))

    expected_data_size = int(sock.recv(4).decode())

    received_data = ''
    while len(received_data) < expected_data_size:
        received_data += sock.recv(4).decode()
    print("Resposta do servidor: " + received_data)
    
    if received_data == "see ya":
        aux = False
    else:
        mensagem = input("MSG >> ")
        send_data_size = len(mensagem)
        sock.sendall(str(send_data_size).zfill(4).encode())

        sock.sendall(mensagem.encode())
        if mensagem == "see ya":
            aux = False

    sock.close()

print("Finalizando...")