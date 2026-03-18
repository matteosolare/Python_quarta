import socket

IP_PORTA = ("localhost", 12345)
BUFFER_SIZE = 4096
SEPARATORE = "|"
def main():
    #rubrica utenti:
    rubrica = {"luca":("192.168.100.2", 54617)}
    #creazione di un socket IPv4 UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #lego socket a IP + PORTA
    s.bind(IP_PORTA)

    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE)
        print(f"Ricevuto {dati.decode()} da {ip_porta_mittente}")

    #il server deve capire se il messaggio ricevuto è di HELLO oppure di chat
    #se è un messaggio di HELLO allora aggiorna la rubrica, se è un messaggio di chat allora lo inoltra

        campi = dati.decode().split(SEPARATORE)
        if dati.decode().upper() =="EXIT":
            break
    
    s.close()

if __name__=="__main__":
    main()