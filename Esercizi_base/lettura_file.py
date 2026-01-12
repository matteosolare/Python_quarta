file = open("./dati.csv", "r") # oggetto file
#il file ha tante righe
righe = file.readlines() #restituisce una lista di stringhe che contiene le righe del file
file.close()

print(righe[0])#stampa il primo elemento della lista

titoli = righe[0][:-1].split(",") #titoli è una lista
print(titoli)

titolo1, titolo2, titolo3 = righe[0][:-1].split(",") #stampa i titoli da soli
print(titolo1)

#leggere tutte le altre righe del file e stamparle
#uso un ciclo for pythonico (NO range)

