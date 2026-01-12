ALFABETO = "abcdefghijklmnopqrstuvwxyz"

def stampa_frequenze(dizionario, percentuali, alfabeto):
    """
    La funzione stampa le frequenze delle lettere fornite.
    Input: 
        - dizionario: contiene le frequenze assolute per tutte le lettere
        - alfabeto: stringa contenente le lettere di interesse
    Output: 
        - None
    """
    print("="*78)
    for lettera in alfabeto:
        if lettera in dizionario:
            print(f"{lettera} - {dizionario[lettera]} - {percentuali[lettera]:.2f}%")
        else:
            print(f"{lettera} - 0 - 0.00%")
    print("="*78)

def calcola_percentuale(dizionario, tot_lettere):
    """
    Todo
    """
    #Calcoliamo percentuali usando una COMPREHENSION
    percentuali = {lettera:(dizionario[lettera] * 100)/tot_lettere for lettera in dizionario}
    return percentuali

def main():
    print("Apertura file...")
    file = open("testo.txt", "r")
    testo = file.read()
    file.close()
    print(f"Letti {len(testo)} caratteri.")
    print()

    lettere_diz = {}
    tot_lettere = 0

    for carattere in testo:
        if carattere.isalpha():
            lettera = carattere.lower()
            tot_lettere += 1
            if lettera in lettere_diz:
                lettere_diz[lettera] += 1
            else:
                lettere_diz[lettera] = 1
    percentuali = calcola_percentuale(lettere_diz, tot_lettere)
    stampa_frequenze(lettere_diz, percentuali, ALFABETO)
        
if __name__ == "__main__":
    main()

#Scrivere un programma che:
#legga un file di testo (ad esempio i  Promessi Sposi o qualsiasi altro testo italiano). Costruisca un dizionario che
#  associ ad ogni lettera il suo conteggio.Calcoli la frequenza percentuale di ogni lettera.
# Specifiche
#Ignorare maiuscole/minuscole (trattare 'A' come 'a')
#Ignorare spazi, punteggiatura, numeri — contare solo le 26 lettere dell'alfabeto base
#Il file di input si chiama testo.txt
#Suggerimenti
#str.isalpha() restituisce True se il carattere è una lettera
#str.lower() converte in minuscolo