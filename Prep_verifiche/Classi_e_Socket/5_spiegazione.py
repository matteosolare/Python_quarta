from threading import Thread
import time

class Thread:
    def __init__(self, nome, secondi):
        super().__init__()       # inizializza la classe madre Thread
        self.nome = nome         # nome del cronometro (es. "A")
        self.secondi = secondi   # durata in secondi (es. 2)

    # run() viene chiamato automaticamente da .start()
    # contiene il codice che il thread esegue in parallelo
    def cronometro(self):
        print(f"{self.nome} avviato")
        time.sleep(self.secondi)  # aspetta 'secondi' secondi
        print(f"{self.nome} terminato dopo {self.secondi} s")

def main():
    # creo tre cronometri con nomi e durate diverse
    # ma non li avvio ancora
    t1 = Thread("A", 2)
    t2 = Thread("B", 4)
    t3 = Thread("C", 1)

    inizio = time.time()  # salvo il tempo prima di avviare i thread

    # start() avvia i thread — tutti e tre partono quasi contemporaneamente
    # non aspetta che finiscano, va subito alla riga successiva
    t1.start()
    t2.start()
    t3.start()

    # join() blocca il main finché il thread non termina
    t1.join()  # aspetta A (2s)
    t2.join()  # aspetta B (4s)
    t3.join()  # aspetta C (1s, ma è già finito da tempo)

    fine = time.time()
    print(f"tutti i cronometri sono terminati in {fine - inizio:.2f} s")

    # Il tempo totale è circa 4s (il più lungo), non 2+4+1=7s.
    # I thread girano in PARALLELO: A, B e C partono insieme,
    # quindi si aspetta solo il più lento.

if __name__ == "__main__":
    main()