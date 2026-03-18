import socket 
SERVER_CHAT = ("127.0.0.1", 12345) #LO STESSO PER TUTTI I CLIENT
NICKNAME = "JHONDOE" #ogni client ha il suo
SEPARATORE = "|"
def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #crea un socket

    #implementare un messaggio di HELLO in cui il client si presenta al server

    messaggio = input("DESTINATARIO | MESSAGGIO -> ") #stringa
    campi = messaggio.split("|")
    if len(campi) == 2:
        dest, mess = campi
        s.sendto(f"{dest}{SEPARATORE}{mess}".encode(), SERVER_CHAT)
    else:
        print("ERRORE")



    s.close()


if __name__ == "__main__":
    main()