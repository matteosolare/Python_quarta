# creare un server ed un client TCP. Il client manda messaggi al server e, 
# per ogni messaggoi che manda, riceve indietro una risposta con il suffisso SERVER:(messaggio inviato). 
# SE l'utente invia exit, server e client si chiudono

import socket

host = "localhost"
port = 1100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen()
print("Il server è in ascolto")

conn, address = s.accept()
print(f"Nuova connessione da {address}")

while True:
    messaggio = conn.recv(1024)
    messaggio = messaggio.decode()
    print(f"Ricevuto: {messaggio}")
    
    if messaggio == "exit":
        conn.send("exit".encode()) 
        break
    else:
        risposta = f"SERVER: {messaggio}"  
        conn.send(risposta.encode())      

s.close()


