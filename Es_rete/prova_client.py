import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #crea un socket
    DESTINATARIO = ("192.168.1.116", 13000)
    messaggio = input("-> ")
    s.sendto(messaggio.encode(), DESTINATARIO)
    s.close()
if __name__ == "__main__":
    main()