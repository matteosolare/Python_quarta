import socket

porta = 1100
ip = "localhost"

# creo il socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bisogna connettere il socket al socket del server
s.connect((ip, porta)) # stabilisce la connessione con il server

while True:
    messaggio = input("Messaggio: ")
    messaggio_cod = messaggio.encode()
    s.sendall(messaggio_cod)
    if messaggio == "exit":
        break
s.close()