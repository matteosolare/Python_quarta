import socket

SERVER_CHAT = ("localhost", 12345) # lo stesso per tutti i client
NICKNAME = "JohnDoe" # ogni client ha il suo
SEPARATORE = " | "

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # implementare un messaggio di HELLO (benvenuto) in cui il client si presenta al server
    s.sendto(f"Server | Il mio nome è '{NICKNAME}'".encode(), SERVER_CHAT)

    while True:
        messaggio = input("DESTINATARIO | MESSAGGIO -> ")

        campi = messaggio.split(SEPARATORE)
        if len(campi) == 2:
            dest, mess = campi
            s.sendto(f"{dest}{SEPARATORE}{mess}".encode(), SERVER_CHAT)
            if mess.upper() == "EXIT": break

        else:
            print("errore")

    s.close()


if __name__ == "__main__":
    main()