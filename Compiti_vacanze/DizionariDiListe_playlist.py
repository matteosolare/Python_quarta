# Un dizionario associa nomi di playlist a liste di titoli di canzoni. Scrivere funzioni per:
# (a) contare le canzoni totali, (b) cercare in quale playlist si trova una canzone, (c) unire
# due playlist in una nuova.

def conta_canzoni_tot(playlist):
    
    lista = []
    tot = 0

    for chiave in playlist:
        for canzone in playlist[chiave]:
            lista.append(canzone)
            tot = tot + 1
    
    print("Il totale di canzoni è: ")
    return tot



def cerca_canzone(playlist, canzone_cercata):

    for chiave in playlist:
        for canzone in playlist[chiave]:
            if canzone == canzone_cercata:
                print("La canzone cercata si trova nella playlist: ")
                print(chiave)



#def unione_playlist(playlist, playlist1, playlist2):

    #playlist_nuova = []

    #for playlist1 in playlist:
    #    if playlist1 not in playlist_nuova:
     #       playlist_nuova.append(playlist1)

#    for playlist2 in playlist:
 #       if playlist2 not in playlist_nuova:
  #          playlist_nuova.append(playlist2) 

 #   return playlist_nuova



def main():

    playlist = {
    "Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
    "Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
    "Relax": ["Hotel California", "Imagine", "Let It Be"]
    }

    print(conta_canzoni_tot(playlist))
    cerca_canzone(playlist, "Imagine")
   # print(unione_playlist(playlist, "Rock", "Pop"))

if __name__ == "__main__":
    main()
