# Si vuole un server UDP che restituisca al client lo stesso messaggio ricevuto, preceduto dal
# numero progressivo di richieste servite dall'avvio del server.

# Tutti i messaggi sono stringhe ASCII.
# • Il client invia una stringa qualunque (es. ciao mondo).
# • Il server risponde con <n> <stringa_ricevuta> dove <n> è il numero progressivo 
# (la prima richiesta ha n=1).
                                                     
# Parte 1 — server (50%)
# Realizzare server_echo.py:
# 1 Crea un socket UDP e fa il bind sulla porta 5006.
# 2 Mantiene un contatore intero n, inizializzato a 0.
# 3 In ciclo infinito riceve un datagramma, incrementa n, costruisce la risposta e la invia al
# mittente.
# 4 Stampa a video ogni richiesta ricevuta con IP e porta del client.

import socket

BUFFERSIZE = 4096

def main():

    host = "localhost"
    porta = 5006

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, porta))

    n = 0
    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFERSIZE)
        stringa = dati.decode()
        n += 1
        messaggio = f"{n} {stringa}"
        s.sendto(messaggio.encode(), ip_porta_mittente)
        print(f"Richiesta da {ip_porta_mittente}: {stringa}")

if __name__ == "__main__":
    main()