# PROCESSO SERVER: colui che eroga servizi, per esempio di comunicazione.

import socket #built in: nativa

def main():
    # 1)CREAZIONE SOCKET
    # Un socket è un AND-POINT di comunicazione (la cornetta telefonica)
                            # IPv4           UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #crea un socket

    # 2)SOLO SUL SERVER (DI SOLITO): LEGARE IL SOCKET A INSIRIZZO IP + PORTA 
    # LA PORTA è UN NUMERO A 16 BIT CHE INDIRIZZA UN PROCESSO NEL COMPUTER
    # LE PORTE MINORI DI 1024 SI CHIAMANO WELL-KNOWN (NON USARE)
    IP_PORTA = ("127.0.0.1", 13000)
    s.bind(IP_PORTA) # LEGA IL SOCKET A IP E PORTA

    # ORA IL SOCKET PUò ESSERE USATO PER COMUNICARE
    BUFFER_SIZE = 4096
    while True:
        #I DATI SONO STRINGHE BINARIE, vanno decodificati
        dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE) # BLOCCANTE!! riceve dalla scheda di rete e mette dentro un 
        #                                                               buffer: gli passiamo la buffer size
        # restituisce dati e ip porta del mittente
        stringa = dati.decode() #trasforma i dati binari in stringhe
        print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")
        if stringa.upper() == "EXIT":
            break

    #CHIUDE IL SOCKET
    s.close()


if __name__ == "__main__":
    main()