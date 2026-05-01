# Data una lista, restituire una nuova lista contenente gli stessi 
# elementi ma senza duplicati, mantenendo l’ordine di prima apparizione.

def Restituisce_elem_senza_duplicati(elementi):

    elementi_senza_duplicati = []

    for elemento in elementi:
        if elemento not in elementi_senza_duplicati:
            elementi_senza_duplicati.append(elemento)

    print(elementi_senza_duplicati)

def main():

    elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]
    Restituisce_elem_senza_duplicati(elementi)

if __name__ == "__main__":
    main()