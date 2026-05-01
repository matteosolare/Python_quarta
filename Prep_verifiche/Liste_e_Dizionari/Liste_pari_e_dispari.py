# Data una lista di interi, scrivere una funzione che restituisca 
# due liste separate: una con i numeri pari e una con i dispari.

def Separa_Pari_Dispari(numeri):

    pari = []
    dispari = []

    for numero in numeri:
        if numero % 2 == 0:
            pari.append(numero)
        else:
            dispari.append(numero)
    return pari, dispari

def main():

    numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]
    pari, dispari = Separa_Pari_Dispari(numeri)
    print(pari)
    print(dispari)

if __name__ == "__main__":
    main()