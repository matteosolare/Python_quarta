# Un dizionario associa nomi di materie a liste di voti. Scrivere funzioni per: (a) calcolare
# la media di una materia, (b) trovare la materia con media più alta, (c) aggiungere un
# voto a una materia.

def calcola_media(voti_materie, materia):

    return sum(voti_materie[materia])/len(voti_materie[materia])



def calcola_media_piu_alta(voti_materie):

    media_max = 0

    for materia in voti_materie:
        media = sum(voti_materie[materia])/len(voti_materie[materia])
        for _ in voti_materie[materia]:
            if media > media_max :
                media_max = media

    return media_max



def add_voto(voti_materie, materia):

    voto = 8
    voti_materie[materia].append(voto)
    return voti_materie[materia]



def main():

    voti_materie = {
    "Matematica": [6, 7, 5, 8, 7],
    "Italiano": [7, 8, 7, 6],
    "Inglese": [8, 8, 9, 7, 8],
    "Informatica": [9, 8, 9, 10, 8]
    }

    print(calcola_media(voti_materie, "Matematica"))
    print(calcola_media_piu_alta(voti_materie))
    print(add_voto(voti_materie, "Italiano"))

if __name__ == "__main__":
    main()
