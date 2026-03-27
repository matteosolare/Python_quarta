import socket

IP_PORTA = ("localhost", 12345)
BUFFER_SIZE = 4096
SEPARATORE = " | "
LOG_LEVEL = "DEBUG"

def log(stringa, tipo):
    """
    stringa = stringa stampata in output
    tipo = INFO, DEBUG o ERROR
    """
    if (tipo.upper() == "DEBUG") and (LOG_LEVEL == "DEBUG"):
        print(f"[DEBUG]: {stringa}")
    elif (tipo.upper() == "INFO"):
        print(f"[INFO]: {stringa}")
    elif (tipo.upper() == "ERROR"):
        print(f"[ERROR]: {stringa}")

def main():
    # rubrica utenti
    rubrica = {}

    # socket IPv4 UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # lego socket a IP e Porta
    s.bind(IP_PORTA)

    #print(f"SERVER: Indirizzo IP ({IP_PORTA[0]}), Porta ({IP_PORTA[1]})")
    log(f"SERVER: Indirizzo IP ({IP_PORTA[0]}), Porta ({IP_PORTA[1]})", "DEBUG")

    while True:
        dati, ipPortaMittente = s.recvfrom(BUFFER_SIZE)
        log(f"Ricevuto <{dati.decode()}> da {ipPortaMittente}", "DEBUG")

        # il server deve capire se il messaggio ricevuto è di HELLO, oppure di chat
        # se è di HELLO, aggiornare la rubrica
        # se è di chat, inoltrarlo (LO FACCIAMO INSIEME)

        campi = dati.decode().split(SEPARATORE)
        if len(campi) == 2:
            dest, mess = campi
        else:
            log("Messaggio malformato", "ERROR")
            continue # ricomincia il ciclo da capo

        if dest == "Server":
            if mess.upper() == "EXIT": break
            
            mess2 = mess.split("'")
            if len(mess2) > 1 and mess2[1] not in rubrica:
                rubrica[mess[1]] = ipPortaMittente
                print(rubrica)


    s.close()


if __name__ == "__main__":
    main()