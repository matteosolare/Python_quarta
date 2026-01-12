#stampare la media di ognuno
#stampare il numero di voti per ognuno
#stampo voto massimo e minimo di ognuno

def main():
    lista_nomi = ["alice", "luca", "giovanni", "mario"]
    lista_voti = [[6, 10, 5], [7, 6], [9, 9], [5, 8]]

    for nome, voti in zip(lista_nomi, lista_voti):
        media = sum(voti) / len(voti)
        voto_max = max(voti)
        voto_min = min(voti)

        somma = 0
        n_voti = len(voti)
        for voto in voti:
            somma = somma + voto
            if voto > voto_max:
                voto_max = voto
            if voto < voto_min:
                voto_min = voto
        media = somma / n_voti

        print(f"\nI voti dell'alunno {nome[0].upper() + nome[1:]}: {voti}")
        print(f"Ecco la media dei voti di {nome[0].upper() + nome[1:]}: {media}")
        print(f"{nome[0].upper() + nome[1:]} ha {n_voti} voti")
        print(f"Ecco il voto più alto che ha preso {nome[0].upper() + nome[1:]}: {voto}")

if __name__=="__main__": #dunder doppio underscore si usa per molti contesti
                         #in questo caso è una variabile
    main()