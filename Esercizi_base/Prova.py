file = open("txt.txt", "r")
righe = file.readlines()
file.close()

diz = {}

for riga in righe:
    campi = riga.split(":")
    chiave = campi[0]
    valori = campi[1].split(",")
    diz[chiave] = valori
print(diz)


