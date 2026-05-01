from threading import Thread

class SommaParziale(Thread):
    def __init__(self, lista):
        super().__init__()
        self.lista = lista
        self.risultato = 0

    def run(self):
        for n in self.lista:
            self.risultato += n

def main():
    
    listaDati = list(range(1, 1000001))
    nThread = 4
    liste = []
    lunghezza = len(listaDati)
    for k in range(nThread):
        indice1 = int(len(listaDati) * k /4)
        indice2 = int(lunghezza * k / nThread)
        liste.append(listaDati[indice1:indice2])

    threads = [SommaParziale(lista) for lista in liste]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    somma = 0
    for t in threads:
        somma += t.risultato
    
    print(f"La somma totale è {somma}")
    print(f"La somma totale è {sum(listaDati)}")

if __name__=="__main__":
    main()