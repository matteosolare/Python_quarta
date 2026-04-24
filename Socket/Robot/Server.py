import socket 
from turtle import Turtle, Screen #CLASSE TURTLE

alphabot = Turtle()         #Istanza Turtle
screen = Screen()

def main():
    alphabot.forward(100)
    #il server deve ricevere messaggi con questo formato: 
    #f"{comando}, {valore}"
    #a seconda del messaggio ricevuto esegue il comando sulla turtle
    #creare un server udp che sta in ascolto di messaggi
    #verifica che i messaggi ricevuti siano formattati correttamente, 
    #se il messaggio è corretto esegue il comando e manda "ok" al client
    #altrimenti manda "error" (e non segue niente)
    #seguire il comando EXIT


    #bonus: client implementare il client utilizzando la libreria pyinput
    screen.mainloop()
if __name__=="__main__":
    main()