import socket

IP_PORTA = ("localhost", 5005)
BUFFER = (4096)

def main():

    diz = {"Cuneo":24, "Milano":20, "Roma":32, "Napoli":35, "Palermo":38}
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(IP_PORTA)

    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFER)
        stringa = dati.decode()
        print(f"Ho ricevuto: {stringa} da {ip_porta_mittente}")

        _ , localita = stringa.split(" ")

        if localita.lower() in diz:
            messaggio = f"TEMP {localita} {diz[localita]}"
        else:
            messaggio = "ERR città sconosciuta"

        s.sendto(messaggio.encode(), ip_porta_mittente)
        s.close()

if __name__ == "__main__":
    main()