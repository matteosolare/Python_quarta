# Dati due dizionari, crearne uno nuovo che contenga tutte le chiavi. 
# Se una chiave è presente in entrambi, sommare i valori.

def main():

    vendite_gennaio = {"mele": 120, "pere": 85, "arance": 200}
    vendite_febbraio = {"mele": 95, "banane": 150, "arance": 180}
    diz_unione = {}

    for chiave in vendite_gennaio:
        quantita = vendite_gennaio[chiave]
        if chiave not in diz_unione:
            diz_unione[chiave] = quantita

    for chiave in vendite_febbraio:
        quantita = vendite_febbraio[chiave]
        if chiave not in diz_unione:
            diz_unione[chiave] = quantita
        else:
            diz_unione[chiave] += quantita
    print(diz_unione)      

if __name__ == "__main__":
    main()






