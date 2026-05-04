# Parte 2 — client (50%)
# Realizzare client_calc.py:
# 1 Crea un socket UDP.
# 2 Chiede all'utente operazione e operandi con input().
# 3 Invia la richiesta al server in ascolto su 127.0.0.1:5007.
# 4 Riceve la risposta e la stampa.
# 5 Termina dopo una sola richiesta.

import socket

BUFFERSIZE = 4096

def main():

    host = "localhost"
    porta = 5007
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    operazione = input("Inserisci l'operazione: ")
    s.sendto(operazione.encode(), (host, porta))
    dati, _ = s.recvfrom(BUFFERSIZE)
    print(dati.decode())
    s.close()

if __name__ == "__main__":
    main()