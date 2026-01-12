def main():
    lista_nomi = ["alice", 
                  "luca", 
                  "giovanni", 
                  "mario"]
    lista_voti = [[6, 10, 5],
                  [7, 6],
                  [9, 9],
                  [5, 8]]

    #stampare la media di ognuno
    #stampare il numero di voti per ognuno
    #stampo voto massimo e minimo di ognuno

    #voglio stampare il voto a fianco di ogni nome
    for nome, voto in zip(lista_nomi, lista_voti):
        print(f"{nome}: {voto}")
    #zip() mi permette di ciclare in parallelo su due o più liste

if __name__=="__main__": #dunder doppio underscore si usa per molti contesti
                         #in questo caso è una variabile
    main()