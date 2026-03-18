# PROCESSO CLIENT: colui che sfrutta i servizi, per esempio di comunicazione.

import socket #built in: nativa

def main():
    # 1)CREAZIONE SOCKET
    # Un socket è un AND-POINT di comunicazione (la cornetta telefonica)
                            # IPv4           UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #crea un socket
    DESTINATARIO = ("127.0.0.1", 13000)
    messaggio = input("-> ") #stringa

    s.sendto(messaggio.encode(), DESTINATARIO)

    #CHIUDE IL SOCKET
    s.close()


if __name__ == "__main__":
    main()