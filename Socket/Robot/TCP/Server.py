import socket
# porte: da 0 a 65535, 0 a 1023 non le posso utilizzare perchè le usa il sistema operativo
# il server deve ascoltare, ricevere dei messaggi e rispondere

# 1. scelgo un indirizzo ip e una porta su cui avviare il server
host = "127.0.0.1"
porta = 1025

# 2. creo il socket iPv4 TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET: tipo di indirizzo ip che stiamo utilizzando (iPv4)
                                                      # SOCK_STREAM: tipo di socket (TCP) 
                                                      # SOCK_DGRAM: UDP

# 3. collego il socket alla porta e all'ip che ho scelto
# s.bind(host, porta) 
s.bind((host, porta)) # tupla, gli passo un parametro che contiene indirizzo ip e porta  

# 4. metto in ascolto il mio server TCP
s.listen()
print("Il server sta ascoltando sulla porta 1025")

# 5. accetto la connessine al server
conn, address = s.accept() 
print(f"Nuova connessione da {address}")

# 6. il server fa quello che deve fare (in questo caso stampa tutti i messaggi che il client manda)
while True:
    messaggio = conn.recv(1024) # aspetta di ricevere un messaggio dalla connessione che è appena stata stabilita, 
                                # 1024 è la grandezza del messaggio che si aspetta (1024 byte)
    messaggio = messaggio.decode()
    print(f"Ricevuto il messaggio: {messaggio}")
    if messaggio == "exit":
        break

# 7. chiudo il socket
s.close()


# 1. scelgo un indirizzo ip e una porta su cui avviare il server
# 2. creare il socket ipV4 TCP
# 3. collego il socket alla porta e all'ip scelti
# 4. mettere in ascolto il server
# 5. accetto la connessione al server
# 6. il server fa quello che deve fare (in questo caso stampa tutti i messaggi che il client manda)
# 7. chiudo il socket
