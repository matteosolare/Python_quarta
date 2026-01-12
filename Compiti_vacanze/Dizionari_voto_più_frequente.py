# Dato un dizionario che associa nomi di studenti ai loro voti 
# (un voto per studente), trovare quale voto compare più spesso.

def main():

    studenti_voti = {
    "Marco": 7,
    "Sara": 8,
    "Luca": 6,
    "Elena": 8,
    "Paolo": 7,
    "Giulia": 8,
    "Andrea": 6,
    "Chiara": 7
    }

    voti = []
    for nome in studenti_voti:
        voti.append(studenti_voti[nome])
    print(voti)

    for voto in voti:
        pass

if __name__ == "__main__":
    main()