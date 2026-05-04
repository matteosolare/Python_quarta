# Esercizio 4 — calcolatrice remota su UDP

# Si vuole un servizio di calcolo elementare: il client invia un'operazione, 
# il server risponde con il risultato.
# Protocollo
# Tutti i messaggi sono stringhe ASCII.
# • Il client invia: <operazione> <a> <a>, <b> sono numeri interi (esempio: add 7 5).
# <b> dove <operazione> è una di add, sub, mul, div e
# • Il server risponde:
# ■ RES <risultato> se l'operazione è valida (esempio: RES 12);
# ■ ERR operazione sconosciuta se l'operazione non è tra le quattro previste;
# ■ ERR divisione per zero nel caso specifico di div con b = 0.

# Parte 1 — server (50%)
# Realizzare server_calc.py:
# 1 Crea un socket UDP e fa il bind sulla porta 5007.
# 2 un ciclo infinito riceve un datagramma, decodifica il comando, controlla con un if quale
# operazione è stata richiesta e se è ammissibile, costruisce la risposta 
# corrispondente e la invia al mittente.
# 3 Stampa a video ogni richiesta ricevuta.

import socket

BUFFERSIZE = 4096

def main():

    host = "localhost"
    porta = 5007
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, porta))

    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFERSIZE)
        print("esempio comando: add 7 5, le operazioni possibili sono: add, sub, mul, div\n")
        stringa = dati.decode()
        campi = stringa.split(" ")
        operazione = campi[0]
        a = int(campi[1])
        b = int(campi[2])
        if operazione == "add":
            risposta = f"RES {a + b}"
        elif operazione == "sub":
            risposta = f"RES {a - b}"
        elif operazione == "mul":
            risposta = f"RES {a * b}"
        elif operazione == "div":
            if b == 0:
                risposta = "ERR: divisione per zero"
            else:
                risposta = f"RES {a / b}"
        else:
            risposta = "ERR: operazione sconosciuta"

        s.sendto(risposta.encode(), ip_porta_mittente)

if __name__ == "__main__":
    main()
