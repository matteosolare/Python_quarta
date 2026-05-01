import socket 

BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    citta = input("Città: ")
    DESTINATARIO = ("127.0.0.1", 5005)

    messaggioCompleto = "GET " + citta

    s.sendto(messaggioCompleto.encode(), DESTINATARIO)

    dati, _ = s.recvfrom(1024)
    stringa = dati.decode()

    print(stringa)

    s.close() 

if __name__ == "__main__":
    main()
