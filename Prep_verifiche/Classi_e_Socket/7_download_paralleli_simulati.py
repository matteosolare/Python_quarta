# Esercizio 7 — download paralleli simulati
# Contesto
# Si vuole simulare il download di più file in parallelo. Ogni download è rappresentato da una
# funzione che dorme per un tempo prefissato.

# Specifiche
# Scrivere una funzione scarica(url, durata) che:
# 1 stampa download di <url> iniziato;
# 2 esegue time.sleep(durata);
# 3 stampa download di <url> completato in <durata> s.
# Nel main, eseguire due volte la stessa lista di download (almeno 5 elementi, con durate tra 1 e 4
# secondi):
# 1 la prima volta in modo sequenziale, con un semplice ciclo for che chiama direttamente
# scarica;
# 2 la seconda volta in modo parallelo, avviando un thread per ciascun download e attendendoli
# tutti con join().
# Per entrambe le modalità misurare il tempo totale con time.time() e stamparlo. Riportare in un
# commento il rapporto tra i due tempi e spiegare perché il tempo parallelo è approssimativamente
# pari alla durata del download più lungo.

import time
import random
from threading import Thread

def scarica(url, durata):
    print(f"download di {url} iniziato")
    time.sleep(durata)
    print(f"download di {url} completato in {durata}s\n")

def main():

    downloads = [
        "youtube.com",
        "google.com",
        "netflix.com",
        "spotify.com",
        "github.com",
    ]

    i = 0
    for url in downloads:
        scarica(downloads[i], random.randint(1, 4))
        i += 1

    # creo un thread per ogni download
    threads = []
    for url, durata in downloads:
        t = Thread(target=scarica, args=(url, durata))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
