# Esercizio 5 — cronometri paralleli
# Contesto
# Si vogliono avviare più cronometri indipendenti, ciascuno eseguito in un thread separato. 
# Ogni cronometro attende un certo numero di secondi e poi stampa un messaggio.

# Specifiche
# Scrivere una funzione cronometro(nome, secondi) che:
# 1 stampa <nome> avviato;
# 2 attende secondi secondi con time.sleep(secondi);
# 3 stampa <nome> terminato dopo <secondi> s.

# Nel main:
# 1 creare almeno tre thread con threading.Thread(target=cronometro,
# args=(...,)), con nomi e durate diverse (es. A con 2 s, B con 4 s, C con 1 s);

# 2 avviare tutti i thread con start();

# 3 attendere la terminazione di ciascuno con join();

# 4 stampare alla fine tutti i cronometri sono terminati.

# Domanda
# Misurando il tempo con time.time() prima dello start del primo thread e dopo l'ultimo join,
# verificare che il tempo totale è circa pari alla durata del cronometro più lungo, non alla somma di
# tutte le durate. Spiegare in un commento al codice perché.

from threading import Thread
import time

class Thread:
    def __init__(self, nome, secondi):
        super().__init__()  
        self.nome = nome      
        self.secondi = secondi   
    
    def cronometro(self):
        print(f"{self.nome} avviato")
        time.sleep(self.secondi)
        print(f"{self.nome} terminato dopo {self.secondi} s")

def main():

    t1 = Thread("A", 2)
    t2 = Thread("B", 4)
    t3 = Thread("C", 1)

    inizio = time.time()  

    t1.start()
    t2.start()
    t3.start()

    t1.join()  
    t2.join()  
    t3.join()  

    fine = time.time()
    print(f"tutti i cronometri sono terminati in {fine - inizio:.2f} s")

if __name__ == "__main__":
    main()