# Dato un dizionario italiano-inglese e una frase in italiano, restituire la frase tradotta. 
# Se una parola non è nel dizionario, lasciarla invariata.
def main():

    diz = {
    "ciao": "hello",
    "mondo": "world",
    "casa": "house",
    "gatto": "cat",
    "cane": "dog",
    "libro": "book",
    "albero": "tree"
    }

    frase = "ciao mondo il gatto è in casa"
    frase_tradotta = ""
    parole = frase.split()
    i = 0

    for i in range(len(parole)):
        parola = parole[i]
        if parola in diz:
            frase_tradotta += diz[parola]
        else:
            frase_tradotta += parola
        frase_tradotta += " "
    print(frase_tradotta)

if __name__ == "__main__":
    main()