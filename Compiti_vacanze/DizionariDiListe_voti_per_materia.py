# Un dizionario associa nomi di materie a liste di voti. Scrivere funzioni per: (a) calcolare
# la media di una materia, (b) trovare la materia con media più alta, (c) aggiungere un
# voto a una materia.

def calcola_media(voti_materie, materia):

    return sum(voti_materie[materia])/

def main():

    voti_materie = {
    "Matematica": [6, 7, 5, 8, 7],
    "Italiano": [7, 8, 7, 6],
    "Inglese": [8, 8, 9, 7, 8],
    "Informatica": [9, 8, 9, 10, 8]
    }

if __name__ == "__main__":
    main()
