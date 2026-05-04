# Parte 2 — client (50%)
# Realizzare client_echo.py:
# 1 Crea un socket UDP.
# 2 Legge una stringa con input().
# 3 Invia la stringa al server in ascolto su 127.0.0.1:5006.
# 4 Riceve la risposta e la stampa.
# 5 Termina dopo una sola richiesta.

import socket

BUFFERSIZE = 4096

def main():

    host = "localhost"
    porta = 5006
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    stringa = input("Inserisci il messaggio: ")
    s.sendto(stringa.encode(), (host, porta))
    dati, _ = s.recvfrom(BUFFERSIZE)
    print(dati.decode())
    s.close()


if __name__ == "__main__":
    main()