# Data una stringa, costruire un dizionario che 
# associ a ogni carattere il numero di volte che compare.

def main():

    testo = "abracadabra"

    print(f"Testo: {testo}")

    conteggio = {}
    
    for carattere in testo:
        if carattere in conteggio:
            conteggio[carattere] += 1
        else:
            conteggio[carattere] = 1
    print(conteggio)
    
if __name__ == "__main__":
    main()